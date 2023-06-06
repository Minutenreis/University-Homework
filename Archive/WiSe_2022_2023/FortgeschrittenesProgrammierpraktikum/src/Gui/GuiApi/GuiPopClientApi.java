package GuiApi;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Properties;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.mail.Authenticator;
import javax.mail.BodyPart;
import javax.mail.Folder;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Store;
import javax.mail.internet.MimeMultipart;

import org.jsoup.Jsoup;

import GuiApi.User.POP3PROTOCOL;

//https://kodejava.org/how-do-i-receive-mail-using-pop3/
public class GuiPopClientApi {
    // username "Minutenreis@gmx.de";
    // password "TestPasswordGithub";
    // server "pop.gmx.net";
    // port 995;

    public Message[] receiveMail(User user) throws Exception {
        // 1. Setup properties for the mail session.
        Properties props;
        if (user.pop3Protocol == POP3PROTOCOL.SSL) {
            props = configPropertiesSSL(user);
        } else if (user.pop3Protocol == POP3PROTOCOL.NO_SSL) {
            props = configPropertiesNoSSL(user);
        } else {
            throw new Exception("POP3 Protocol not set");
        }

        // 2. Creates a javax.mail.Authenticator object.
        Authenticator auth = new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(user.username, user.password);
            }
        };

        // 3. Creating mail session.
        Session session = Session.getInstance(props, auth);

        // 4. Get the POP3 store provider and connect to the store.
        Store store = session.getStore("pop3");
        store.connect(user.pop3Server, user.pop3Port, user.username, user.password);

        // 5. Get folder and open the INBOX folder in the store.
        Folder inbox = store.getFolder("INBOX");
        inbox.open(Folder.READ_ONLY);

        // 6. Retrieve the messages from the folder.
        // int messageCount = inbox.getMessageCount();
        Message[] messages = inbox.getMessages();

        // 6.5 Write to disk
        writeToDisk(messages, user);

        // 7. Close folder and close store.

        return messages;
    }

    private void writeToDisk(Message[] messages, User user) throws Exception {
        for (Message message : messages) {
            new File("mails/" + user.username).mkdirs();
            File file = new File("mails/" + user.username + "/" + createFileName(message) + ".eml");
            if (file.isFile()) { // don't save stuff double
                continue;
            }
            ByteArrayOutputStream output = new ByteArrayOutputStream();
            message.writeTo(output);
            OutputStream outputStream = new FileOutputStream(file);
            output.writeTo(outputStream);
        }
    }

    public static String createFileName(Message msg) throws Exception {
        String fileName = msg.getSubject() + "-" + msg.getSentDate() + "-" + msg.getFrom()[0];

        Pattern p = Pattern.compile("[^a-zA-Z0-9_-]");
        Matcher m = p.matcher(fileName);

        return m.replaceAll("");
    }

    private Properties configPropertiesSSL(User user) {
        Properties props = new Properties();
        props.put("mail.pop3.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.pop3.socketFactory.fallback", "false");
        props.put("mail.pop3.socketFactory.port", user.pop3Port);
        props.put("mail.pop3.port", user.pop3Port);
        props.put("mail.pop3.host", user.pop3Server);
        props.put("mail.pop3.user", user.username);
        props.put("mail.store.protocol", "pop3");
        props.put("mail.pop3.ssl.protocols", "TLSv1.2");
        return props;
    }

    private Properties configPropertiesNoSSL(User user) {
        Properties props = new Properties();
        props.put("mail.pop3.socketFactory.fallback", "false");
        props.put("mail.pop3.socketFactory.port", user.pop3Port);
        props.put("mail.pop3.port", user.pop3Port);
        props.put("mail.pop3.host", user.pop3Server);
        props.put("mail.pop3.user", user.username);
        props.put("mail.store.protocol", "pop3");
        return props;
    }

    // https://stackoverflow.com/a/34689614
    public static String getTextFromMessage(Message message) throws MessagingException, IOException {
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
    private static String getTextFromMimeMultipart(
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
