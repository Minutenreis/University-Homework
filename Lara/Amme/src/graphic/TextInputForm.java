package graphic;

import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

//ask for textInput and save it to StringBuilder
class TextInputForm extends DisposablePanel{
    TextInputForm(StringBuilder sb){
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        JTextArea textArea = new JTextArea(30,50); //2Dimensional
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        addSubPanel(new JScrollPane(textArea));

        JButton submit = new JButton("Submit");
        submit.addActionListener(e ->{
                sb.append(textArea.getText());
                dispose.run();
            }
        );
        addSubPanel(submit);

        JButton cancel = new JButton("Cancel");
        cancel.addActionListener(e -> {
                dispose.run();
            });
        addSubPanel(cancel);
    }

    void addSubPanel(Component comp) {
        JPanel subPanel = new JPanel();
        subPanel.add(comp);
        add(subPanel);
    }
}