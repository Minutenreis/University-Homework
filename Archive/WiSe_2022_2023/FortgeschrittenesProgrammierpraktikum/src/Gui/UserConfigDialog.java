import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

import javax.swing.BoxLayout;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

import java.awt.*;

import GuiApi.User;
import GuiApi.User.POP3PROTOCOL;
import GuiApi.User.SMTPPROTOCOL;

public class UserConfigDialog extends DisposablePanel {

    public UserConfigDialog(User user, boolean cancelable) {
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        JLabel usernameLabel = new JLabel("Username");
        Component[] usernameLabels = { usernameLabel };
        addSubPanel(usernameLabels);

        JTextField usernameText = new JTextField(user.username != null? user.username : "Minutenreis@gmx.de", 20);
        usernameText.setMaximumSize(usernameText.getPreferredSize());
        Component[] usernameTexts = { usernameText };
        addSubPanel(usernameTexts);

        JLabel passwordLabel = new JLabel("Password");
        Component[] passwordLabels = { passwordLabel };
        addSubPanel(passwordLabels);

        JPasswordField passwordText = new JPasswordField(user.password != null? user.password : "TestPasswordGithub", 20);
        passwordText.setMaximumSize(passwordText.getPreferredSize());
        Component[] passwordTexts = { passwordText };
        addSubPanel(passwordTexts);

        JLabel pop3ServerLabel = new JLabel("Pop3-Server");
        JLabel smtpServerLabel = new JLabel("Smtp-Server");

        Component[] serverLabels = { pop3ServerLabel, smtpServerLabel };
        addSubPanel(serverLabels);

        JTextField pop3ServerText = new JTextField(user.pop3Server != null? user.pop3Server : "pop.gmx.net", 20);
        pop3ServerText.setMaximumSize(pop3ServerText.getPreferredSize());
        JTextField smtpServerText = new JTextField(user.smtpServer != null? user.smtpServer : "mail.gmx.net", 20);
        smtpServerText.setMaximumSize(smtpServerText.getPreferredSize());

        Component[] serverTexts = { pop3ServerText, smtpServerText };
        addSubPanel(serverTexts);

        JLabel pop3PortLabel = new JLabel("Pop3-Port");
        JLabel smtpPortLabel = new JLabel("Smtp-Port");

        Component[] portLabels = { pop3PortLabel, smtpPortLabel };
        addSubPanel(portLabels);

        JTextField pop3PortText = new JTextField(user.pop3Port != null ? Integer.toString(user.pop3Port ) : "995", 20);
        pop3PortText.setMaximumSize(pop3PortText.getPreferredSize());
        JTextField smtpPortText = new JTextField(user.smtpPort != null? Integer.toString(user.smtpPort)  : "587", 20);
        smtpPortText.setMaximumSize(smtpPortText.getPreferredSize());

        Component[] portTexts = { pop3PortText, smtpPortText };
        addSubPanel(portTexts);

        JRadioButton sslButtonPop3 = new JRadioButton("SSL", user.pop3Protocol != null ? user.pop3Protocol == POP3PROTOCOL.SSL: true);
        JRadioButton noSslButtonPop3 = new JRadioButton("No-SSL", user.pop3Protocol != null ? user.pop3Protocol == POP3PROTOCOL.NO_SSL: false);

        ButtonGroup bGroupPop3 = new ButtonGroup();
        bGroupPop3.add(sslButtonPop3);
        bGroupPop3.add(noSslButtonPop3);

        JPanel radioPanelPop3 = new JPanel();
        radioPanelPop3.setLayout(new GridLayout(2, 1));
        radioPanelPop3.add(sslButtonPop3);
        radioPanelPop3.add(noSslButtonPop3);

        JRadioButton tlsButtonSmtp = new JRadioButton("TLS", user.smtpProtocol != null ? user.smtpProtocol == SMTPPROTOCOL.TLS : true);
        JRadioButton sslButtonSmtp = new JRadioButton("SSL", user.smtpProtocol != null ? user.smtpProtocol == SMTPPROTOCOL.SSL : false);
        JRadioButton noSslButtonSmtp = new JRadioButton("No-SSL", user.smtpProtocol != null ? user.smtpProtocol == SMTPPROTOCOL.NO_SSL : false);

        ButtonGroup bGroupSmtp = new ButtonGroup();
        bGroupSmtp.add(tlsButtonSmtp);
        bGroupSmtp.add(sslButtonSmtp);
        bGroupSmtp.add(noSslButtonSmtp);

        JPanel radioPanelSmtp = new JPanel();
        radioPanelSmtp.setLayout(new GridLayout(3, 1));
        radioPanelSmtp.add(tlsButtonSmtp);
        radioPanelSmtp.add(sslButtonSmtp);
        radioPanelSmtp.add(noSslButtonSmtp);

        Component[] radioBtns = { radioPanelPop3, radioPanelSmtp };

        addSubPanel(radioBtns);

        JButton btnSaveAndClose = new JButton("save");
        btnSaveAndClose.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                user.username = usernameText.getText();
                user.password = new String(passwordText.getPassword());
                user.pop3Server = pop3ServerText.getText();
                user.pop3Port = Integer.parseInt(pop3PortText.getText());
                user.smtpServer = smtpServerText.getText();
                user.smtpPort = Integer.parseInt(smtpPortText.getText());
                if (tlsButtonSmtp.isSelected()) {
                    user.smtpProtocol = User.SMTPPROTOCOL.TLS;
                } else if (sslButtonSmtp.isSelected()) {
                    user.smtpProtocol = User.SMTPPROTOCOL.SSL;
                } else if (noSslButtonSmtp.isSelected()) {
                    user.smtpProtocol = User.SMTPPROTOCOL.NO_SSL;
                }
                if (sslButtonPop3.isSelected()) {
                    user.pop3Protocol = POP3PROTOCOL.SSL;
                } else if (noSslButtonPop3.isSelected()) {
                    user.pop3Protocol = POP3PROTOCOL.NO_SSL;
                }
                saveUserToFile(user);
                dispose.run();
            }
        });

        JButton btnCancel = new JButton("cancel");
        btnCancel.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if (cancelable) {
                    dispose.run();
                } else {
                    System.exit(0);
                }
            }
        });
        Component[] configBtns = { btnSaveAndClose, btnCancel };
        addSubPanel(configBtns);
    }

    void addSubPanel(Component[] comp) {
        JPanel subPanel = new JPanel();
        for (Component c : comp) {
            subPanel.add(c);
        }
        add(subPanel);
    }

    void saveUserToFile(User user) {
        try {
            new File("mails").mkdir();
            FileOutputStream fileOut = new FileOutputStream(new File("mails/" + "user.ser"));
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            System.out.print(new File("mails/" + "user.ser").getAbsolutePath());
            out.writeObject(user);
            out.close();
            fileOut.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
