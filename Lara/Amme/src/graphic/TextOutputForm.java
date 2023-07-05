package graphic;

import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class TextOutputForm extends DisposablePanel {

    public TextOutputForm(String text) {
        this.setLayout(new BorderLayout());
        JTextArea textArea = new JTextArea(text, 30, 50);
        textArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(textArea);
        this.add(scrollPane, BorderLayout.CENTER);

        JButton closeButton = new JButton("Close");
        closeButton.addActionListener(e -> {
                dispose.run();
            }
        );
        this.add(closeButton, BorderLayout.SOUTH);
    }
}