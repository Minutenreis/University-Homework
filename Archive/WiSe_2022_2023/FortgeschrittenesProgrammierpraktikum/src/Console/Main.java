package Console;
import java.util.Scanner;

import Console.Api.PopClientApi;
import Console.Api.SmtpClientApi;
import Console.Socket.PopClientSocket;
import Console.Socket.SmtpClientSocket;

public class Main {
    public static void main(String[] args) throws Exception {

        final Scanner scanner = new Scanner(System.in);
        System.out.println("Receive API: 1\nReceive Socket: 2 \nSend API: 3\nSend Socket: 4");
        int option = Integer.parseInt(scanner.nextLine());
        switch (option) {
            case 1:
                // Java Mail
                PopClientApi popClientM = new PopClientApi(scanner);
                popClientM.receiveMail();
                break;
            case 2:
                // Socket
                PopClientSocket popClientS = new PopClientSocket(scanner);
                popClientS.receiveMail();
                break;
            case 3:
                // Java Mail
                SmtpClientApi smtpClientM = new SmtpClientApi(scanner);
                smtpClientM.sendMail();
                break;
            case 4:
                // Socket
                SmtpClientSocket smtpClientS = new SmtpClientSocket(scanner);
                smtpClientS.sendMail();
                break;
            default:
                System.out.println("Keine Implementation");
                break;
        }
        scanner.close();
    }
}
