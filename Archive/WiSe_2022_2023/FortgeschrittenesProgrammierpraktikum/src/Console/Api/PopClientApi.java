package Console.Api;

import javax.mail.*;
import javax.mail.internet.MimeMultipart;

import org.jsoup.Jsoup;

import java.io.IOException;

import java.util.*;

//https://kodejava.org/how-do-i-receive-mail-using-pop3/
public class PopClientApi {
    // username "Minutenreis@gmx.de";
    // password "TestPasswordGithub";
    // server "pop.gmx.net";
    // port 995;

    Scanner sc;

    public PopClientApi(Scanner sc) {
        this.sc = sc;
    }

    public void receiveMail() throws Exception {
        // 1. Setup properties for the mail session.
        System.out.println("Enter your POP3 Server: ");
        String server = sc.nextLine();
        System.out.println("Enter your POP3 Port: ");
        int port = Integer.parseInt(sc.nextLine());
        System.out.println("Enter your email address: ");
        String username = sc.nextLine();
        //https://stackoverflow.com/questions/12076165/how-to-obscure-scanner-input-text
        String password = new String(System.console().readPassword("Enter your password: "));
        Properties props;
        if (port == 995) {
            props = configPropertiesSSL(server, port, username);
        } else if (port == 110) {
            props = configPropertiesNoSSL(server, port, username);
        } else {
            System.out.println("SSL? (y/n)");
            String ssl = sc.nextLine();
            props = ssl == "n" ? configPropertiesNoSSL(server, port, username)
                    : configPropertiesSSL(server, port, username);
        }

        // 2. Creates a javax.mail.Authenticator object.
        Authenticator auth = new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        };

        // 3. Creating mail session.
        Session session = Session.getInstance(props, auth);

        // 4. Get the POP3 store provider and connect to the store.
        Store store = session.getStore("pop3");
        store.connect(server, port, username, password);

        // 5. Get folder and open the INBOX folder in the store.
        Folder inbox = store.getFolder("INBOX");
        inbox.open(Folder.READ_ONLY);

        // 6. Retrieve the messages from the folder.
        Message[] messages = inbox.getMessages();

        while (true) {
            // Input message
            System.out.println(getTextFromMessage(chooseMessage(messages, sc)));
            System.out.println("\n Wollen Sie eine andere Nachricht lesen? (y/n)");
            String input = sc.nextLine();
            if (input.equals("n")) {
                break;
            }
        }

        System.out.println("See you later, alligator!");
        // 7. Close folder and close store.
        inbox.close(false);
        store.close();
    }

    // Gibt n-te Email aus
    private Message chooseMessage(Message[] messages, Scanner sc) throws Exception {
        System.out.println("Total messages: " + messages.length);
        System.out.println("Welche Nachricht wollen Sie sich anschauen?");
        // Ausgabe der Emails
        for (int i = 0; i < messages.length; i++) {
            System.out.println(
                    i + "\tSubject: " + messages[i].getSubject() + "\n\tFrom: " + messages[i].getFrom()[0].toString());
        }
        int n;
        while (true) {
            n = Integer.parseInt(sc.nextLine());
            if (n >= 0 && n < messages.length) {
                break;
            }
            System.out.println("Bitte geben Sie eine Zahl zwischen 0 und " + (messages.length - 1) + " ein");
        }
        return messages[n];
    }

    private Properties configPropertiesSSL(String server, int port, String username) {
        Properties props = new Properties();
        props.put("mail.pop3.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.pop3.socketFactory.fallback", "false");
        props.put("mail.pop3.socketFactory.port", port);
        props.put("mail.pop3.port", port);
        props.put("mail.pop3.host", server);
        props.put("mail.pop3.user", username);
        props.put("mail.store.protocol", "pop3");
        props.put("mail.pop3.ssl.protocols", "TLSv1.2");
        return props;
    }

    private Properties configPropertiesNoSSL(String server, int port, String username) {
        Properties props = new Properties();
        props.put("mail.pop3.socketFactory.fallback", "false");
        props.put("mail.pop3.socketFactory.port", port);
        props.put("mail.pop3.port", port);
        props.put("mail.pop3.host", server);
        props.put("mail.pop3.user", username);
        props.put("mail.store.protocol", "pop3");
        return props;
    }

    // https://stackoverflow.com/a/34689614
    private String getTextFromMessage(Message message) throws MessagingException, IOException {
        String result = "";
        if (message.isMimeType("text/plain")) {
            result = message.getContent().toString();
        } else if (message.isMimeType("multipart/*")) {
            MimeMultipart mimeMultipart = (MimeMultipart) message.getContent();
            result = getTextFromMimeMultipart(mimeMultipart);
        }
        return result;
    }

    // https://stackoverflow.com/a/34689614
    private String getTextFromMimeMultipart(
            MimeMultipart mimeMultipart) throws MessagingException, IOException {
        String result = "";
        int count = mimeMultipart.getCount();
        for (int i = 0; i < count; i++) {
            BodyPart bodyPart = mimeMultipart.getBodyPart(i);
            if (bodyPart.isMimeType("text/plain")) {
                result = result + "\n" + bodyPart.getContent();
                break; // without break same text appears twice in my tests
            } else if (bodyPart.isMimeType("text/html")) {
                String html = (String) bodyPart.getContent();
                result = result + "\n" + Jsoup.parse(html).text();
            } else if (bodyPart.getContent() instanceof MimeMultipart) {
                result = result + getTextFromMimeMultipart((MimeMultipart) bodyPart.getContent());
            }
        }
        return result;
    }
}
