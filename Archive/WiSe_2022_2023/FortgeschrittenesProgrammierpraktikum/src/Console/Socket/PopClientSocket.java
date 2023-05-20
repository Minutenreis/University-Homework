package Console.Socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

import javax.net.ssl.SSLSocketFactory;

// http://mike-java.blogspot.com/2008/03/simple-pop3-client-in-java-tutorial.html
public class PopClientSocket {
    Socket socket;
    private BufferedReader reader;
    private PrintWriter writer;
    private boolean debug = false;
    Scanner sc;

    String testUsername = "Minutenreis@gmx.de";
    String testPassword = "TestPasswordGithub";
    String testServer = "pop.gmx.net";
    int testPort = 995;

    public PopClientSocket(Scanner sc) {
        this.sc = sc;
    }

    public String[] receiveMail() throws IOException {
        debug = true;
        connect(sc);
        login(testUsername, testPassword);
        int stat = getMessageQuantity();
        System.out.println("Sie haben " + stat + " Nachrichten");
        while (true) {
            // Input message
            System.out.println("Enter message number: ");
            int messageNumber = Integer.parseInt(sc.nextLine());
            retrieve(messageNumber, reader);
            System.out.println("\n Wollen Sie eine andere Nachricht lesen? (y/n)");
            String input = sc.nextLine();
            if (input.equals("n")) {
                break;
            }
        }
        // List<Message> list = getAllMessages();
        disconnect();
        socket.close();
        return null;
    }

    // Retrieve Message
    public void retrieve(int messageNumber, BufferedReader reader) throws IOException {
        if(sendCommand("RETR " + messageNumber).startsWith("-ERR")) {
            System.out.println("Error retrieving message");
            return;
        }
        boolean text = false;
        while (true) {
            String line = reader.readLine();
            if (line.equals(".")) {
                break;
            }
            if (line.startsWith("Content-Type: text/plain")){
                text = true;
            } else if (line.startsWith("--")){
                text = false;
            }
            if(text){
                System.out.println(line);
            //important headers
            } else if(line.startsWith("From:") || line.startsWith("Subject:") || line.startsWith("Date:") || line.startsWith("To:")){
                System.out.println(line);
            }
        }
    }

    // connect to the server
    public void connect(Scanner sc) throws IOException {
        if (testPort == 995) {
            connectSSL(testServer, testPort);
        } else if (testPort == 110) {
            connectNoSSL(testServer, testPort);
        } else {
            System.out.println("SSL? (y/n)");
            String ssl = sc.nextLine();
            if (ssl.equals("n")) {
                connectNoSSL(testServer, testPort);
            } else {
                connectSSL(testServer, testPort);
            }
        }
    }

    // printed Befehle aus
    public void setDebug(boolean debug) {
        this.debug = debug;
    }

    // erstellt SSL Socket
    public void connectSSL(String host, int port) throws IOException {
        socket = SSLSocketFactory.getDefault().createSocket(host, port);
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        writer = new PrintWriter(socket.getOutputStream(), true);
        if (debug) {
            System.out.println("Connected to the " + host + " on port " + port);
        }
        readResponseLine();
    }

    // erstellt Socket ohne SSL
    public void connectNoSSL(String host, int port) throws IOException {
        socket = new Socket(host, port);
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        writer = new PrintWriter(socket.getOutputStream(), true);
        if (debug) {
            System.out.println("Connected to the " + host + " on port " + port);
        }
        readResponseLine();
    }

    // Liest die Antwortzeile
    protected String readResponseLine() throws IOException {
        String response = reader.readLine();
        if (debug) {
            System.out.println(response);
        }
        return response;
    }

    // Sendet command an die Socket
    protected String sendCommand(String command) throws IOException {
        if (debug) {
            System.out.println(command);
        }
        writer.println(command);
        return readResponseLine();
    }

    public void login(String username, String password) throws IOException {
        sendCommand("USER " + username);
        sendCommand("PASS " + password);
    }

    public void logout() throws IOException {
        sendCommand("QUIT");
    }

    // POP3 STAT: +OK "Anzahl" "Größe in Bytes"
    public int getMessageQuantity() throws IOException {
        String response = sendCommand("STAT");
        String[] values = response.split(" ");
        return Integer.parseInt(values[1]);
    }

    public boolean isConnected() {
        return socket != null && socket.isConnected();
    }

    public void disconnect() throws IOException {
        if (!isConnected()) {
            throw new IllegalStateException("Not connected");
        }
        socket.close();
        reader = null;
        writer = null;
        if (debug) {
            System.out.println("Disconnected");
        }
    }

}
