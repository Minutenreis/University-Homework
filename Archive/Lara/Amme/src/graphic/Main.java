package graphic;

import java.awt.Component;
import java.awt.Dialog;
import java.awt.GridLayout;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import com.github.sh0nk.matplotlib4j.Plot;

import client.MyGenBankClient;

public class Main {
    private JFrame window;
    private MyGenBankClient client;

    public Main(){
        window = new JFrame();
        window.setTitle("Client");
        window.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE); //Schließen, wenn auf Kreuz klicken
        window.setSize(1000,400);
        window.setLocationRelativeTo(null); //Mittige Anzeige
        window.setLayout(new GridLayout(0,1));

        client = new MyGenBankClient();
        client.startClient();

        LoginForm login = new LoginForm(client);
        createModalDialog(window, "Login", login).setVisible(true);

        //Error
        JLabel status = new JLabel("");
        addSubPanel(status);


        JButton putBtn = new JButton("Put");
        putBtn.addActionListener(e -> { //eine Methode e, einfachere Schreibweise
            StringBuilder sb = new StringBuilder("");
            TextInputForm put = new TextInputForm(sb);
            createModalDialog(window, "Put", put, 800, 600).setVisible(true);
            if(sb.length() > 0){
                try {
                    String response = client.put(sb.toString());
                    status.setText(response);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
            }
        });
        addSubPanel(putBtn);

        JButton EMBLBtn = new JButton("EMBL");
        EMBLBtn.addActionListener(e -> { // eine Methode e, einfachere Schreibweise
            StringBuilder sb = new StringBuilder("");
            TextInputForm EMBL = new TextInputForm(sb);
            createModalDialog(window, "EMBL", EMBL, 800, 600).setVisible(true);
            if (sb.length() > 0) {
                try {
                    String response = client.EMBL(sb.toString());
                    createModalDialog(window, "EMBL", new TextOutputForm(response), 800, 600).setVisible(true);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
            }
        });
        addSubPanel(EMBLBtn);

        JButton GenBankBtn = new JButton("GenBank");
        GenBankBtn.addActionListener(e -> { // eine Methode e, einfachere Schreibweise
            StringBuilder sb = new StringBuilder("");
            TextInputForm genBank = new TextInputForm(sb);
            createModalDialog(window, "GenBank", genBank, 800, 600).setVisible(true);
            if (sb.length() > 0) {
                try {
                    String response = client.GenBank(sb.toString());
                    createModalDialog(window, "GenBank", new TextOutputForm(response), 800, 600).setVisible(true);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
            }
        });
        addSubPanel(GenBankBtn);

        JButton dotBtn = new JButton("Dotplot");
        dotBtn.addActionListener(e -> { // eine Methode e, einfachere Schreibweise
            StringBuilder name1 = new StringBuilder("");
            StringBuilder name2 = new StringBuilder("");
            SelectGenBank selectGenBankDialog = new SelectGenBank(name1, name2, client);
            createModalDialog(window, "Dotplot", selectGenBankDialog, 800, 600).setVisible(true);
            try {
                if(name1.length() == 0 || name2.length() == 0){
                    return;
                }
                String response = client.dotplot(name1.toString(), name2.toString());
                dotPlotVisualizer(response);
            } catch (IOException e1) {
                e1.printStackTrace();
            }
        });
        addSubPanel(dotBtn);
        window.setVisible(true);

    }
    public static JDialog createModalDialog(JFrame parent, String title, DisposablePanel content) {
        return createModalDialog(parent, title, content, 350, 300);
    }

    public static JDialog createModalDialog(JFrame parent, String title, DisposablePanel content, int width, int height) {
        final JDialog dialog = new JDialog(parent, title, Dialog.ModalityType.DOCUMENT_MODAL);
        dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        dialog.getContentPane().add(content);
        dialog.pack();
        dialog.setSize(width, height);
        dialog.setLocationRelativeTo(parent);
        content.dispose = () -> dialog.dispose();
        return dialog;
    }

    void addSubPanel(Component comp) {
        JPanel subPanel = new JPanel();
        subPanel.add(comp);
        window.add(subPanel);
    }

    public static void main(String[] args) {
        //später darkmode
        //UIManager.setLookAndFeel("com.formdev.flatlaf.FlatDarkLaf");
        new Main();

    }

    public void dotPlotVisualizer(String dotplot){
        List<Double> xVals = new ArrayList<>();
        List<Double> yVals = new ArrayList<>();
        StringBuilder yLegend = new StringBuilder();
        StringBuilder xLegend = new StringBuilder();
        String[] rows = dotplot.split("\n");
        rows[0].split("|");
        for(int i = 2; i < rows[0].length()-1; i+=2){
            yLegend.append(rows[0].charAt(i));
        }
        for(int i = 1; i < rows.length; i++){
            String[] cols = rows[i].split("|");
            System.out.println(Arrays.toString(cols));

            xLegend.append(cols[0]);
            for(int j = 1; j < cols.length-1; j++){
                if(cols[j].equals("*")){
                    xVals.add((double) i);
                    yVals.add((double) j/2);
                }
            }
        }
        System.out.println(xVals.size() + " " + yVals.size());
        for(int i = 0; i < xVals.size(); i++){
            System.out.println(xVals.get(i) + " " + yVals.get(i));
        }
        Plot plt = Plot.create();
        plt.plot().add(xVals, yVals, "*"); //Punkt im Graph
        plt.title("Dotplot");
        plt.xlabel(xLegend.toString());
        plt.ylabel(yLegend.toString());
        try{
            plt.show();
        } catch (Exception e){
            e.printStackTrace();
        }
    }

    
}
