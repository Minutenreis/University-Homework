package graphic;

import java.awt.GridLayout;
import java.io.IOException;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import client.MyGenBankClient;

public class SelectGenBank extends DisposablePanel {
    public SelectGenBank(StringBuilder name1, StringBuilder name2, MyGenBankClient client) {
        this.setLayout(new GridLayout(0, 2));
        String optionString = "";
        try {
            optionString = client.getAllNames().trim();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String[] options = optionString.split(" ");

        JLabel status1 = new JLabel("");
        JLabel status2 = new JLabel("");

        JRadioButton dropdown1 = new JRadioButton("Dropdown", true);
        JRadioButton manual1 = new JRadioButton("Manual", false);

        ButtonGroup bGroup1 = new ButtonGroup();
        bGroup1.add(dropdown1);
        bGroup1.add(manual1);

        JRadioButton dropdown2 = new JRadioButton("Dropdown", true);
        JRadioButton manual2 = new JRadioButton("Manual", false);

        ButtonGroup bGroup2 = new ButtonGroup();
        bGroup2.add(dropdown2);
        bGroup2.add(manual2);

        this.add(dropdown1);
        this.add(dropdown2);
        this.add(manual1);
        this.add(manual2);

        JComboBox<String> name1Box = new JComboBox<String>(options);
        JComboBox<String> name2Box = new JComboBox<String>(options);
        this.add(name1Box);
        this.add(name2Box);

        JTextArea name1Input = new JTextArea(20, 30);
        name1Input.setLineWrap(true);
        name1Input.setWrapStyleWord(true);
        JScrollPane scroll1 = new JScrollPane(name1Input);

        JTextArea name2Input = new JTextArea(20, 30);
        name2Input.setLineWrap(true);
        name2Input.setWrapStyleWord(true);
        JScrollPane scroll2 = new JScrollPane(name2Input);

        this.add(scroll1);
        this.add(scroll2);

        // name1 either dropdown or input; if input => put it to server first

        JButton submit = new JButton("Submit");
        submit.addActionListener(e -> {
            if (dropdown1.isSelected()) {
                name1.append((String) name1Box.getSelectedItem());
            } else if (manual1.isSelected()) {
                name1.append(putAndGetName(name1Input.getText(), client, status1));
            }
            if (dropdown2.isSelected()) {
                name2.append((String) name2Box.getSelectedItem());
            } else if (manual2.isSelected()) {
                name2.append(putAndGetName(name2Input.getText(), client, status2));
            }
            if(name1.toString().equals("") || name2.toString().equals("")) {
                return;
            }
            dispose.run();
        });
        this.add(submit);

        JButton cancel = new JButton("Cancel");
        cancel.addActionListener(e -> dispose.run());
        this.add(cancel);
    }

    public String putAndGetName(String content, MyGenBankClient client, JLabel status) {
        try {
            String response = client.put(content);
            status.setText("Status: " + response);
            return response.split("'")[1];
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "";
    }

}
