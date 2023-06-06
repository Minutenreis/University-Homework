package GuiApi;

import java.util.*;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class GuiSmtpClientApi {
    // username "Minutenreis@gmx.de";
    // password "TestPasswordGithub";
    // server "mail.gmx.net";
    // port 587;

    // https://www.digitalocean.com/community/tutorials/javamail-example-send-mail-in-java-smtp
    public void sendMail(User user, GuiBasicMessage basicMessage) throws Exception {
        if (!basicMessage.isValid()) {
            throw new Exception("Message is not valid");
        }

        // 1. Setup properties for the mail session.

        Properties props = setProperties(user);

        Session session;

        if (user.smtpProtocol != User.SMTPPROTOCOL.NO_SSL) {
            Authenticator auth = new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(user.username, user.password);
                }
            };
            session = Session.getInstance(props, auth);
        } else {
            session = Session.getInstance(props);
        }

        // 6. Create a message.
        Message message = new MimeMessage(session);

        // 8. Set Content
        message.setFrom(new InternetAddress(user.username));
        message.setSubject(basicMessage.subject);
        message.setText(basicMessage.body);
        message.setSentDate(new Date());
        message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(basicMessage.to));
        if (!basicMessage.cc.equals("")) {
            message.addRecipients(Message.RecipientType.CC, InternetAddress.parse(basicMessage.cc));
        }
        // 9. Send the message.
        Transport.send(message, message.getAllRecipients());
    }

    Properties configPropertiesNoSSL(User user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", user.smtpServer);
        props.put("mail.smtp.port", user.smtpPort);
        props.put("mail.smtp.starttls.enable", "false");
        return props;
    }

    Properties configPropertiesTLS(User user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", user.smtpServer);
        props.put("mail.smtp.port", user.smtpPort);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        return props;
    }

    Properties configPropertiesSSL(User user) {
        Properties props = new Properties();
        props = System.getProperties();
        props.put("mail.smtp.host", user.smtpServer);
        props.put("mail.smtp.port", user.smtpPort);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.socketFactory.port", user.smtpPort);
        props.put("mail.smtp.socketFactory.fallback", "false");
        return props;
    }

    Properties setProperties(User user) throws Exception {
        switch (user.smtpProtocol) {
            case NO_SSL:
                return configPropertiesNoSSL(user);
            case TLS:
                return configPropertiesTLS(user);
            case SSL:
                return configPropertiesSSL(user);
            default:
                throw new Exception("Unknown SMTP Protocol");
        }
    }
}
