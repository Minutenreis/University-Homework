package client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class MyGenBankClient { //private
    Socket socket;
    PrintWriter out;
    BufferedReader in;

    public void startClient() {
        try {
            this.socket = new Socket("localhost", 2367); // localhost -> nachschauen auf eigenem Rechner
            this.out = new PrintWriter(socket.getOutputStream(), true);
            this.in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            System.out.println("**Connected to Server**");
            System.out.println("Client started");
        } catch (Exception e) {
            e.printStackTrace(); // wo kommt der Fehler vor
        }
    }

    public void stopClient() {
        try {
            out.println("exit");
            this.socket.close();
            this.out.close();
            this.in.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //register, login, get, getAllNames, dotplot
    public String sendSingleLineCommand(String command) throws IOException {
        out.println(command);
        return readResponse();
    }

    //put, EMBL, GenBank
    public String sendMultiLineCommand(String command, String content) throws IOException {
        String output = command + "\n" + content;
        System.out.println(output);
        out.println(output);
        return readResponse();
    }

    public String register(String username, String password) throws IOException {
        String command = "register " + username + " " + password;
        return sendSingleLineCommand(command); //wenn Antwort success 
    }
    
    public String login(String username, String password) throws IOException {
        String command = "login " + username + " " + password;
        return sendSingleLineCommand(command);
    }

    public String put(String content) throws IOException {
        String command = "put";
        return sendMultiLineCommand(command, content);
    }

    public String get(String name) throws IOException {
        String command = "get " + name;
        return sendSingleLineCommand(command);
    }

    public String getAllNames() throws IOException {
        String command = "getAllNames";
        return sendSingleLineCommand(command);
    }

    public String EMBL(String content) throws IOException {
        String command = "EMBL";
        return sendMultiLineCommand(command, content);
    }

    public String GenBank(String content) throws IOException {
        String command = "GenBank";
        return sendMultiLineCommand(command, content);
    }

    public String dotplot(String name1, String name2) throws IOException {
        String command = "dotplot " + name1 + " " + name2;
        return sendSingleLineCommand(command);
    }



    public String readResponse() throws IOException {
        String line = in.readLine();
        String response = "";
        do {
            response += line + "\n";
        }   while (in.ready() && (line = in.readLine()) != null);
        System.out.println(response);
        return response;
    }

    public static void main(String[] args) {
        MyGenBankClient client = new MyGenBankClient();
        client.startClient();
    }
}
