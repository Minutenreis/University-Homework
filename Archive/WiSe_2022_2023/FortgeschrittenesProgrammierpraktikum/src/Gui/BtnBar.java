import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JToolBar;

public class BtnBar extends JPanel {
    
    JToolBar toolBar = new JToolBar();

    BtnBar(Runnable writeMail, Runnable openDialog, Runnable reloadMails, Runnable deleteMail){
        JButton btnNewMail = new JButton("New Mail");
        btnNewMail.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                writeMail.run();
            }
        });
        toolBar.add(btnNewMail);

        JButton btnConfig = new JButton("Edit User");
        btnConfig.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                openDialog.run();
            }
        });
        toolBar.add(btnConfig);

        JButton btnReload = new JButton("Reload");
        btnReload.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                reloadMails.run();
            }
        });
        toolBar.add(btnReload);

        JButton btnDelete = new JButton("Delete");
        btnDelete.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                deleteMail.run();
            }
        });
        toolBar.add(btnDelete);

        this.add(toolBar);
    }
}
