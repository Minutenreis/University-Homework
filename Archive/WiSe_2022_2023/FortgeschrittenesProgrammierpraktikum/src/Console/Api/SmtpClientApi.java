package Console.Api;

import java.util.*;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SmtpClientApi {
    // username "Minutenreis@gmx.de";
    // password "TestPasswordGithub";
    // server "mail.gmx.net";
    // port 587;
    Scanner sc;

    public SmtpClientApi(Scanner sc) {
        this.sc = sc;
    }

    //https://www.digitalocean.com/community/tutorials/javamail-example-send-mail-in-java-smtp
    public void sendMail() throws Exception {
        // 1. Setup properties for the mail session.
        System.out.println("Enter your SMTP Server: ");
        String server = sc.nextLine();
        System.out.println("Enter your SMTP Port: ");
        int port = Integer.parseInt(sc.nextLine());
        System.out.println("Enter your email address: ");
        String username = sc.nextLine();
        // https://stackoverflow.com/questions/12076165/how-to-obscure-scanner-input-text
        String password = new String(System.console().readPassword("Enter your password: "));

        System.out.println("Enter recipients (separated by ','): ");
        String recipients = sc.nextLine();
        Address[] recipientsArray = InternetAddress.parse(recipients);

        System.out.println("Enter your subject: ");
        String subject = sc.nextLine();
        System.out.println("Enter your message line by line. Enter '.' to finish.");
        String text = "";
        String nextline;
        while(!(nextline = sc.nextLine()).equals(".")) {
            text += nextline + "\n";
        }

        Properties props = setProperties(server, port, username);

        // have to test whether unencrypted cares for Authenticator
        // boolean encrypted = props.contains(props.get("mail.smtp.starttls.enable"));

        Session session;

        // if(encrypted){
            Authenticator auth = new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(username, password);
                }
            };
            session = Session.getInstance(props, auth);
        // } else {
            // session = Session.getInstance(props);
        // }
        
        // 6. Create a message.
        Message message = new MimeMessage(session);

        //8. Set Content
        message.setFrom(new InternetAddress(username));
        message.setSubject(subject);
        message.setText(text);
        message.setSentDate(new Date());
        message.setRecipients(Message.RecipientType.TO, recipientsArray);

        // 9. Send the message.
        System.out.println("Sending...");
        Transport.send(message, message.getAllRecipients());
        System.out.println("Sent!");
        System.out.println("done?");
        sc.nextLine();
    }

    Properties configPropertiesNoSSL(String server, int port, String user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", server);
        props.put("mail.smtp.port", port);
        props.put("mail.smtp.starttls.enable", "false");
        return props;
    }

    Properties configPropertiesTLS(String server, int port, String user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", server);
        props.put("mail.smtp.port", port);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        return props;
    }

    Properties configPropertiesSSL(String server, int port, String user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", server);
        props.put("mail.smtp.port", port);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.socketFactory.class","javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.socketFactory.port", port);
        props.put("mail.smtp.socketFactory.fallback", "false");
        return props;
    }

    Properties setProperties(String server, int port, String username){
            System.out.println("1: unencrypted\n2: TLS\n3: SSL");
            int encryption = Integer.parseInt(sc.nextLine());
            switch( encryption) {
                case 1:
                    return configPropertiesNoSSL(server, port, username);
                case 2:
                    return configPropertiesTLS(server, port, username);
                case 3:
                    return configPropertiesSSL(server, port, username);
                default:
                    System.out.println("Invalid input. Try again.");
                    return setProperties(server, port, username);
            }
    }
}
