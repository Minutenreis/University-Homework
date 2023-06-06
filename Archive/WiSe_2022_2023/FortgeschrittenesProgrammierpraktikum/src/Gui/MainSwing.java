import javax.swing.UIManager;

public class MainSwing {
    public static void main(String[] args) throws Exception {
        UIManager.setLookAndFeel("com.formdev.flatlaf.FlatDarkLaf");
        MainWindow mainWindow = new MainWindow();
        mainWindow.show();
    }
}
