package server;

import java.net.ServerSocket;

public class MyGenBankServer {
    public static void main(String[] args) {

        try (ServerSocket serverSocket = new ServerSocket(2367)) {
            while (true) {
                new CommunicationThread(serverSocket.accept()).start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
//Verbinden mit dem Client :)