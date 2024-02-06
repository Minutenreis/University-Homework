package graphic;

import java.awt.event.ActionListener;
import java.io.IOException;
import java.awt.event.ActionEvent;
import java.awt.Component;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import client.MyGenBankClient;

public class LoginForm extends DisposablePanel {
    
    public LoginForm(MyGenBankClient client) {
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        //Error
        JLabel errorLabel = new JLabel("");
        addSubPanel(errorLabel);

        //user
        JLabel userLabel = new JLabel("Username");
        addSubPanel(userLabel);

        JTextField userText = new JTextField("LarrySchnarry",20);
        userText.setMaximumSize(userText.getPreferredSize());
        addSubPanel(userText);

        //password
        JLabel passLabel = new JLabel("Password");
        addSubPanel(passLabel);

        JPasswordField passText = new JPasswordField("password", 20); //"*" beim Passwort
        passText.setMaximumSize(passText.getPreferredSize());
        addSubPanel(passText);

        //login button
        JButton button = new JButton("Login");
        button.addActionListener(e -> {
                String username = userText.getText();
                String password = new String(passText.getPassword()); //weil sonst nur Chararray übergeben wird
                try {
                    String response = client.login(username, password);
                    if (!success(response)) {
                        errorLabel.setText(response);
                        return;
                    }
                    dispose.run();
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        });
        addSubPanel(button);

        //register button
        JButton button2 = new JButton("Register");
        button2.addActionListener(e -> {
                String username = userText.getText();
                String password = new String(passText.getPassword()); //weil sonst nur Chararray übergeben wird
                try {
                    String response = client.register(username, password);
                    if (!success(response)) {
                        errorLabel.setText(response);
                        return;
                    }
                    response = client.login(username, password);
                    if (!success(response)) {
                        errorLabel.setText(response);
                        return;
                    }
                    dispose.run();
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        });
        addSubPanel(button2);
    }

    private boolean success(String response){
        return response.startsWith("SUCCESS");
    }

    void addSubPanel(Component comp) {
        JPanel subPanel = new JPanel();
        subPanel.add(comp);
        add(subPanel);
    }
}
