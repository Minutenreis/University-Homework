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

public class MyGenBankClient {
    Socket socket;
    PrintWriter out;
    BufferedReader in;

    public void startClient() {
        try {
            this.socket = new Socket("localhost", 2367); // localhost -> nachschauen auf eigenem Rechner
            this.out = new PrintWriter(socket.getOutputStream(), true);
            this.in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            Scanner scanner = new Scanner(System.in);
            System.out.println("Client started");
            String input = "";
            while (!input.equals("exit")) {
                input = scanner.nextLine();
                if(input.startsWith("put") || input.startsWith("EMBL") || input.startsWith("GenBank")) {
                    String[] args = input.split(" ");
                    String path = args[1];
                    String output = args[0] + "\n";
                    Path p = Paths.get(path);
                    String content = Files.readString(p);
                    output += content;
                    out.println(output);
                } else {
                    out.println(input);
                }
                printResponse();
            }
            out.println("exit");
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace(); // wo kommt der Fehler vor
        }
    }

    public void printResponse() throws IOException {
        String response = in.readLine();
        do {
            System.out.println(response);
        }   while (in.ready() && (response = in.readLine()) != null);
    }

    public static void main(String[] args) {
        MyGenBankClient client = new MyGenBankClient();
        client.startClient();
    }
}
