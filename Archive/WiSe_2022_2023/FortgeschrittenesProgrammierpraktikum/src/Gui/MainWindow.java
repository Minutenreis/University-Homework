import java.awt.Color;
import java.awt.Dialog;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Point;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Date;
import java.util.Properties;
import java.util.spi.CurrencyNameProvider;

import javax.mail.Address;
import javax.mail.Flags;
import javax.mail.Message;
import javax.mail.Session;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeUtility;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.ListSelectionModel;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

import GuiApi.GuiPopClientApi;
import GuiApi.User;

public class MainWindow {

    private JFrame window;
    private User user;

    private JTextArea currentMail = new JTextArea(20, 49);
    private int currentMailIndex = -1;

    private JTable messageTable = new JTable();
    String[] columns = { "Read", "Sent", "Subject", "From", "To", "FileName" };

    public MainWindow() throws Exception {
        loadUser();

        window = new JFrame();
        window.setTitle("Reismail");
        window.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        window.setSize(800, 800);
        window.setLocationRelativeTo(null);
        window.setVisible(true);
        window.setLayout(new FlowLayout());

        // Config Dialog
        if (user == null) {
            user = new User();
            UserConfigDialog mandatoryConfigDialog = new UserConfigDialog(user, false);
            createModalDialog(window, "User Config", mandatoryConfigDialog).setVisible(true);
        }

        UserConfigDialog configDialog = new UserConfigDialog(user, true);

        BtnBar btnBar = new BtnBar(() -> writeMail(),
                () -> createModalDialog(window, "User Config", configDialog).setVisible(true),
                () -> reloadMails(),
                () -> deleteCurrentMail());
        window.add(btnBar);

        Message[] messages = getMessages();

        window.add(createTable(messages));

        currentMail.setEditable(false);
        currentMail.setVisible(true);
        currentMail.setBackground(new Color(40, 40, 40));
        JScrollPane mailScrollPane = new JScrollPane(currentMail);
        mailScrollPane.setPreferredSize(new Dimension(650, 300));
        window.add(mailScrollPane);

    }

    Message[] getMessages() throws Exception {

        try{
            new GuiPopClientApi().receiveMail(user);
        } catch (Exception e) {
            e.printStackTrace();
        }

        Message[] messages = getLocalMessages(user);

        Arrays.sort(messages, compareFnc());
        return messages;
    }

    Comparator<Message> compareFnc() {
        return new Comparator<Message>() {
            @Override
            public int compare(Message o1, Message o2) {
                if (o1 == null && o2 == null)
                    return 0;
                if (o1 == null)
                    return 1;
                if (o2 == null)
                    return -1;
                try {
                    Date d1 = o1.getSentDate();
                    Date d2 = o2.getSentDate();
                    if (d1 == null && d2 == null)
                        return 0;
                    if (d1 == null)
                        return 1;
                    if (d2 == null)
                        return -1;
                    return d2.compareTo(d1);
                } catch (Exception e) {
                    e.printStackTrace();
                    return 0;
                }
            }
        };
    }

    Message[] getLocalMessages(User user) throws Exception {
        Properties props = System.getProperties();
        Session mailSession = Session.getDefaultInstance(props);

        File folder = new File("mails/" + user.username);
        if (!folder.exists()) {
            return new Message[0];
        }
        File[] files = folder.listFiles();

        ArrayList<Message> messages = new ArrayList<Message>();

        for (File file : files) {
            InputStream source = new FileInputStream(file);
            messages.add(new MimeMessage(mailSession, source));
        }
        return messages.toArray(new Message[messages.size()]);
    }

    public JScrollPane createTable(Message[] messages) throws Exception {
        String[][] data = createData(messages);

        messageTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        DefaultTableModel tableModel = new DefaultTableModel() {
            // https://stackoverflow.com/questions/1990817/how-to-make-a-jtable-non-editable
            @Override
            public boolean isCellEditable(int row, int column) {
                // all cells false
                return false;
            }
        };
        tableModel.setDataVector(data, columns);

        messageTable.setModel(tableModel);
        messageTable.setPreferredScrollableViewportSize(messageTable.getPreferredSize());
        messageTable.setFillsViewportHeight(true);

        messageTable.getColumnModel().getColumn(2).setPreferredWidth(400);
        messageTable.removeColumn(messageTable.getColumnModel().getColumn(5));

        ListSelectionModel selectionModel = messageTable.getSelectionModel();

        selectionModel.addListSelectionListener(new ListSelectionListener() {
            public void valueChanged(ListSelectionEvent event) {
                try {
                    selectMessage(event);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

        JScrollPane js = new JScrollPane(messageTable);
        js.setPreferredSize(new Dimension(650, 300));

        return js;
    }

    public void selectMessage(ListSelectionEvent e) throws Exception {
        ListSelectionModel lsm = (ListSelectionModel) e.getSource();
        if (lsm.getValueIsAdjusting() || lsm.getMinSelectionIndex() == -1) {
            return;
        }
        currentMailIndex = lsm.getMinSelectionIndex();

        Message message = getMessage((String) messageTable.getModel().getValueAt(currentMailIndex, 5));

        // get Msg from File

        currentMail.setText(GuiPopClientApi.getTextFromMessage(message));
        currentMail.setCaretPosition(0);
        setRead(message);
        messageTable.getModel().setValueAt("x", currentMailIndex, 0);
        saveMessage(message);
    }

    private void deleteCurrentMail() {
        try {
            if (currentMailIndex == -1) {
                return;
            }
            Message message = getMessage((String) messageTable.getModel().getValueAt(currentMailIndex, 5));
            Message[] remoteMessages = new GuiPopClientApi().receiveMail(user);
            Message folderMsg = null;
            for (Message remoteMessage : remoteMessages) {
                if (GuiPopClientApi.createFileName(remoteMessage).equals(GuiPopClientApi.createFileName(message))) {
                    folderMsg = remoteMessage;
                    break;
                }
            }
            System.out.println("deleting " + folderMsg.getSubject());
            folderMsg.setFlag(Flags.Flag.DELETED, true);
            folderMsg.getFolder().close(true);
            folderMsg.getFolder().getStore().close();
            File file = new File("mails/" + user.username + "/" + GuiPopClientApi.createFileName(message) + ".eml");
            file.delete();
            ((DefaultTableModel) messageTable.getModel()).removeRow(currentMailIndex);
            currentMail.setText("");
            currentMailIndex = -1;
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    private Message getMessage(String filename) throws Exception {
        File file = new File("mails/" + user.username + "/" + filename + ".eml");
        Properties props = System.getProperties();
        Session mailSession = Session.getDefaultInstance(props);

        InputStream source = new FileInputStream(file);
        Message message = new MimeMessage(mailSession, source);
        return message;
    }

    private void saveMessage(Message message) throws Exception {
        File file = new File("mails/" + user.username + "/" + GuiPopClientApi.createFileName(message) + ".eml");
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        message.writeTo(output);
        OutputStream outputStream = new FileOutputStream(file);
        output.writeTo(outputStream);
    }

    public boolean isRead(Message msg) throws Exception {
        String[] header = msg.getHeader("X-Seen");
        return header != null && header[0] != "false";
    }

    private String[][] createData(Message[] messages) throws Exception {
        String[][] data = new String[messages.length][6];
        for (int i = 0; i < messages.length; i++) {
            Message message = messages[i];
            try {
                data[i][0] = isRead(message) ? "x" : "";
            } catch (Exception e) {
                data[i][0] = "";
            }
            try {
                data[i][1] = MimeUtility.decodeText(message.getSentDate().toString());
            } catch (Exception e) {
                data[i][1] = "Unknown";
            }
            try {
                data[i][2] = MimeUtility.decodeText(message.getSubject());
            } catch (Exception e) {
                data[i][2] = "Unknown";
            }
            try {
                data[i][3] = MimeUtility.decodeText(String.join(",", convertAddresses(message.getFrom())));
            } catch (Exception e) {
                data[i][3] = "Unknown";
            }
            try {
                data[i][4] = MimeUtility.decodeText(
                        String.join(",", convertAddresses(message.getRecipients(Message.RecipientType.TO))));
            } catch (Exception e) {
                data[i][4] = "Unknown";
            }
            try {
                data[i][5] = GuiPopClientApi.createFileName(message);
            } catch (Exception e) {
                data[i][5] = "Unkown";
            }
            System.out.println(i);
        }
        return data;
    }

    public void reloadMails() {
        try {
            System.out.println("Reload");
            DefaultTableModel tableModel = (DefaultTableModel) messageTable.getModel();
            Message[] messages = getMessages();
            String[][] data = createData(messages);

            tableModel.setDataVector(data, columns);
            messageTable.getColumnModel().getColumn(1).setPreferredWidth(400);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void setRead(Message msg) throws Exception {
        msg.setHeader("X-Seen", "true");
    }

    public String[] convertAddresses(Address[] addresses) {
        ArrayList<String> stringList = new ArrayList<String>();
        for (Address address : addresses) {
            stringList.add(address.toString());
        }
        return stringList.toArray(new String[stringList.size()]);
    }

    public static JDialog createModalDialog(JFrame parent, String title, DisposablePanel content) {
        final JDialog dialog = new JDialog(parent, title, Dialog.ModalityType.DOCUMENT_MODAL);
        dialog.setDefaultCloseOperation(JDialog.DO_NOTHING_ON_CLOSE);
        dialog.getContentPane().add(content);
        dialog.pack();
        dialog.setSize(800, 600);
        dialog.setLocationRelativeTo(parent);
        content.dispose = () -> dialog.dispose();
        return dialog;
    }

    public void show() {
        window.setVisible(true);
    }

    void loadUser() {
        try {
            File file = new File("mails/user.ser");
            if (!file.exists()) {
                return;
            }
            FileInputStream fileIn = new FileInputStream(file);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            user = (User) in.readObject();
            in.close();
            fileIn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void writeMail() {
        WriteMailDialog writeMailDialog = new WriteMailDialog(user, true);
        createModalDialog(window, "Write new Message", writeMailDialog).setVisible(true);
    }

}
