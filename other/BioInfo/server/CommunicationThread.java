package BioInfo.server;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import BioInfo.shared.Fasta;

public class CommunicationThread extends Thread {
    private Socket socket = null;
    private String username = "";
    private String password = "";
    private static String folder = "genBank/";

    public CommunicationThread(Socket socket) {
        super("CommunicationThread");
        this.socket = socket;
    }

    private Fasta getMyGenBank(String name) throws IOException {
        String filename = folder + name;
        return Fasta.getFastaFromFile(filename);
    }

    private String getNames() {
        File folder = new File("genBank/");
        File[] files = folder.listFiles();
        StringBuilder sb = new StringBuilder();
        for (File file : files) {
            sb.append(file.getName());
            sb.append(" ");
        }
        return sb.toString();
    }

    private void saveMyGenBank(Fasta fasta) throws IOException {
        new File(folder).mkdirs();
        String header = fasta.getHeader().replace(">", "");
        String filename = folder + header + ".fasta";
        int i = 1;
        while (new File(filename).exists()) {
            filename = folder + header + "_" + i + ".fasta";
            i++;
        }
        fasta.writeToFile(filename);
    }

    String createResponse(String in) throws IOException {
        String[] args = in.split(" ");
        if (args.length < 1) {
            return "Invalid command";
        }
        String command = args[0];
        switch (command) {
            case "put": // put <header> <dna>
                System.out.println("put");
                if (args.length < 3) {
                    return "Invalid command";
                }
                saveMyGenBank(new Fasta(args[1], args[2]));
                return "success";
            case "get":
                System.out.println("get");
                if (args.length < 2) {
                    return "Invalid command";
                }
                return getMyGenBank(args[1]).toString();
            case "getNames":
                System.out.println("getNames");
                return getNames();
            case "dotplot":
                System.out.println("dotplot");
                if (args.length < 3) {
                    return "Invalid command";
                }
                return "Multiline\n" + Fasta.dotPlot(getMyGenBank(args[1]).getDNA(), getMyGenBank(args[2]).getDNA())
                        + "End";
            case "EMBL":
                System.out.println("EMBL");
                return ""; // TODO: return MyGenBank
            case "GenBank":
                System.out.println("GenBank");
                return ""; // TODO: return MyGenBank
            default:
                System.out.println("Invalid command");
                return "Invalid command";
        }

    }

    void login(PrintWriter out, BufferedReader in) throws IOException {

        out.println("Username Password:");
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            System.out.println(inputLine);
            String[] login = inputLine.split(" ");
            if (login.length != 2) {
                out.println("Username Password: ");
            } else {
                this.username = login[0];
                this.password = login[1];
                out.println("success");
                return;
            }
        }
    }

    public void run() {
        try (
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));) {
            String inputLine;
            System.out.println("Client connected");
            login(out, in);
            System.out.println("Client logged in");
            while ((inputLine = in.readLine()) != null) {
                System.out.println(inputLine);
                if (inputLine.equals("quit")) {
                    out.println("Bye.");
                    break;
                }
                out.println(createResponse(inputLine));
            }
            System.out.println("Client disconnected");
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
