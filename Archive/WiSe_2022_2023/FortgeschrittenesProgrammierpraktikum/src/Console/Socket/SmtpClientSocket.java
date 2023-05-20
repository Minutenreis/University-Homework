package Console.Socket;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Base64;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

import javax.net.ssl.SSLSocketFactory;

public class SmtpClientSocket {
    Socket socket;
    BufferedReader reader;
    DataOutputStream writer;
    boolean debug = true;
    Scanner sc;

    String testUsername = "minutenreis@gmx.de";
    String testPassword = "TestPasswordGithub";
    String testServer = "mail.gmx.net";
    int testPort = 465;
    boolean ssl = true;

    public SmtpClientSocket(Scanner sc) {
        this.sc = sc;
    }

    public String[] sendMail() throws IOException {
        sendMessage(createMessage(), false);
        disconnect();
        socket.close();
        return null;
    }

    void connect(String host, int port) throws IOException {
        socket = ssl ? SSLSocketFactory.getDefault().createSocket(host, port) : new Socket(host, port);
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        writer = new DataOutputStream(socket.getOutputStream());
        if (debug) {
            System.out.println("Connected to the " + host + " on port " + port);
        }
        readResponseLine();
    }

    void disconnect() throws IOException {
        if (!isConnected()) {
            throw new IllegalStateException("Not connected");
        }
        sendCommand("QUIT");
        socket.close();
        reader = null;
        writer = null;
        if (debug) {
            System.out.println("Disconnected");
        }
    }

    boolean isConnected() {
        return socket != null && socket.isConnected();
    }

    String sendCommand(String command) throws IOException {
        if (debug) {
            System.out.println(command);
        }
        writer.writeBytes(command + "\r\n");
        return readResponseLine();
    }

    protected String readResponseLine() throws IOException {
        String response = reader.readLine();
        if (debug) {
            System.out.println(response);
        }
        return response;
    }

    BasicMessage createMessage() throws IOException {

        List<String> toList = new ArrayList<String>();

        System.out.println("Für wen ist die E-Mail?");
        String input;
        while (!(input = sc.nextLine()).equals("")) {
            toList.add(input);
        }
        String[] to = new String[toList.size()];
        to = toList.toArray(to);

        System.out.println("Betreff der E-Mail?");
        String subject = sc.nextLine();

        System.out.println("Enter your message line by line. Enter '.' to finish.");
        String body = "";
        String nextline;
        while (!(nextline = sc.nextLine()).equals(".")) {
            body += nextline + "\n";
        }
        BasicMessage message = new BasicMessage(body, subject, testUsername, to);
        return message;
    }

    void sendMessage(BasicMessage message, boolean encrypted) throws IOException {
        connect(testServer, testPort);
        if (ssl) {
            sendCommand("EHLO " + testServer);
            readResponseLine();
            readResponseLine();
            readResponseLine();
            sendCommand("AUTH LOGIN");
            sendCommand(Base64.getEncoder().encodeToString(testUsername.getBytes()));
            sendCommand(Base64.getEncoder().encodeToString(testPassword.getBytes()));
        } else {
            sendCommand("HELO " + testServer);
        }

        sendCommand("MAIL FROM: " + testUsername);
        for (int i = 0; i < message.getTo().length; i++) {
            sendCommand("RCPT TO: " + message.getTo()[i]);
        }
        sendCommand("DATA");
        sendData(message);
    }

    void sendData(BasicMessage message) throws IOException {
        writeBytes("From: " + message.getFrom());
        writeBytes("To: " + message.getToString());
        DateFormat dateFormat = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss Z");
        writeBytes("Date: " + dateFormat.format(new Date()));
        writeBytes("Subject: " + message.getSubject());
        writeBytes("");
        writeBytes(message.getBody());
        sendCommand(".\r\n");
    }

    void writeBytes(String bytes) throws IOException {
        if (debug) {
            System.out.println(bytes);
        }
        writer.writeBytes(bytes + "\r\n");
        return;
    }

}