package BioInfo.client;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 4444);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            System.out.println(in.readLine());
            while (true) {
                String inputLine = System.console().readLine();
                out.println(inputLine);
                String serverOutput = in.readLine();
                if (serverOutput.equals("Bye.")) {
                    socket.close();
                    System.exit(0);
                }
                if (serverOutput.equals("Multiline")) {
                    while (!(serverOutput = in.readLine()).equals("End")) {
                        System.out.println(serverOutput);
                    }
                    continue;
                }
                System.out.println(serverOutput);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
