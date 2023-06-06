import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JTextArea;


import GuiApi.GuiBasicMessage;
import GuiApi.GuiSmtpClientApi;
import GuiApi.User;

public class WriteMailDialog extends DisposablePanel {

    public WriteMailDialog(User user, boolean cancelable){
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));


        // Labels & Textfields 
        JLabel recipientLabel = new JLabel("Recipient:");
        Component[] recipientLabelComponents = { recipientLabel };
        addSubPanel(recipientLabelComponents);

        JTextField recipientText = new JTextField(20);
        recipientText.setMaximumSize(recipientText.getPreferredSize());
        Component[] recipientComponents = { recipientText };
        addSubPanel(recipientComponents);

        JLabel ccLabel = new JLabel("CC:");
        Component[] ccLabelComponents = { ccLabel };
        addSubPanel(ccLabelComponents);

        JTextField ccText = new JTextField(20);
        recipientText.setMaximumSize(ccText.getPreferredSize());
        Component[] ccComponents = { ccText };
        addSubPanel(ccComponents);

        JLabel subjectLabel = new JLabel("Subject:");
        Component[] subjectLabelComponents = { subjectLabel };
        addSubPanel(subjectLabelComponents);

        JTextField subjectText = new JTextField(20);
        subjectText.setMaximumSize(subjectText.getPreferredSize());
        Component[] subjectComponents = { subjectText };
        addSubPanel(subjectComponents);

        JLabel messageLabel = new JLabel("Message:");
        Component[] messageLabelComponents = { messageLabel };
        addSubPanel(messageLabelComponents);

        JTextArea messageText = new JTextArea(20,20);
        messageText.setMaximumSize(messageText.getPreferredSize());
        Component[] messageComponents = { messageText };
        addSubPanel(messageComponents);


        // Buttons
        JButton btnSend = new JButton("send");
        btnSend.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {

                String body = messageText.getText();
                String subject = subjectText.getText();
                String from = user.username;
                String recipients = recipientText.getText();
                String cc = ccText.getText();

                GuiBasicMessage message = new GuiBasicMessage(body,subject,from,recipients,cc);
                try {
                    new GuiSmtpClientApi().sendMail(user,message);
                } catch (Exception e1) {
                    e1.printStackTrace();
                }
                dispose.run();
            }
        });

        JButton btnCancel = new JButton("cancel");
        btnCancel.addActionListener(new ActionListener(){
            
            @Override
            public void actionPerformed(ActionEvent e) {
                if (cancelable) {
                    dispose.run();
                } else {
                    System.exit(0);
                }
            }
        });
        Component[] configBtns = { btnSend, btnCancel };
        addSubPanel(configBtns);

    }

    void addSubPanel(Component[] comp) {
        JPanel subPanel = new JPanel();
        for (Component c : comp) {
            subPanel.add(c);
        }
        add(subPanel);
    }
    
}
