package server;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import shared.IllegalHeaderException;
import shared.IllegalSequenceException;
import shared.MyGenBank;

public class CommunicationThread extends Thread {
    private Socket socket;
    private PrintWriter out;
    private BufferedReader in;
    private Boolean loggedIn = false;

    public CommunicationThread(Socket socket) throws IOException { // Fehler wird nach oben weitergereicht (hier
                                                                   // MyGenBankServer)
        super("CommunicationThread");
        this.socket = socket;
        this.out = new PrintWriter(socket.getOutputStream(), true);
        this.in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    public void run() { // bei start() wird run() aufgerufen -> "Main"
        try{
            handleRequest();
        } catch (IOException e) {
            out.println("ERROR: IOException in CommunicationThread.");
            System.out.println("ERROR: IOException in CommunicationThread.");
            e.printStackTrace();
        }    
    }

    public void handleRequest() throws IOException {
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            String[] input = inputLine.split(" ");
            switch (input[0]) { //similiar to if
                case "register": //testing case and switch
                    register(input[1], input[2]);
                    break;
                case "login":
                    loggedIn = login(input[1], input[2]);
                    break;
                case "exit":
                    close();
                    return; //stop, when exit
                //check if logged in
                default:
                    if (!loggedIn) {
                        out.println("ERROR: User not logged in.");
                        break;
                    }
                    switch(input[0]){
                        case "put":
                            putMyGenBank();
                            break;
                        case "getAllNames":
                            out.println(getAllNames());
                            break;
                        case "get":
                            out.println(getMyGenBank(input[1]));
                            break;
                        case "dotplot":
                            out.println(createDotPlot(input[1], input[2]));
                            break;
                        case "EMBL":
                            out.println(EMBLToMyGenBank());
                            break;
                        case "GenBank":
                            out.println(GenBankToMyGenBank());
                            break;
                        default:
                            out.println("ERROR: Command not found.");
                            break;
                    }
            }
        }
    }

    public void close() throws IOException {
        out.close();
        in.close();
        socket.close();
    }

    // register <username> <password>
    private boolean register(String username, String password) {
        Auth auth = new Auth();
        if (username == null || password == null) {
            out.println("ERROR: Username or password is null.");
            return false;
        }

        if (auth.addUser(username, password)) { // userExists() in addUser() enthalten
            out.println("SUCCESS: User registered."); // out.println -> an Server zurückschicken
            return true;
        } else {
            out.println("ERROR: User could not be registered.");
            return false;
        }

    }

    // login <username> <password>
    private boolean login(String username, String password) {
        Auth auth = new Auth();
        if (username == null || password == null) {
            out.println("ERROR: Username or password is null.");
            return false;
        }

        if (auth.checkPassword(username, password)) {
            out.println("SUCCESS: User logged in.");
            return true;
        } else {
            out.println("ERROR: User could not be logged in.");
            return false;
        }
    }

    // put \n<myGenBank>
    // return 1 line
    private void putMyGenBank() throws IOException {
        try{
            MyGenBank myGenBank = MyGenBank.readMyGenBankFile(in);
            if (myGenBank == null) {
                out.println("ERROR: MyGenBank is null.");
                return;
            }
            String filename = myGenBank.getFasta().getHeader().replace(" ", "_") + ".gbk";
            new File("GenBankFiles").mkdirs();// create folder
            myGenBank.toFile("GenBankFiles/" + filename);
            out.println("SUCCESS: MyGenBank '" + filename + "' stored.");
        } catch (IllegalHeaderException e) {
            out.println("ERROR: MyGenBank has illegal Header.");
            return;
        } catch (IllegalSequenceException e) {
            out.println("ERROR: MyGenBank has illegal Sequence.");
            return;
        }
    }

    // getAllNames
    // returns 1 line
    private String getAllNames() {
        File folder = new File("GenBankFiles/");
        File[] files = folder.listFiles();
        if (files == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        for (File file : files) {
            sb.append(file.getName());
            sb.append(" ");
        }
        return sb.toString();

    }

    // get <name>
    // returns MyGenBank (Multiline)
    private MyGenBank getMyGenBank(String name) throws IOException {
        String path = "GenBankFiles/" + name;
        File file = new File(path);
        if (!file.exists()) {
            return null;
        }
        return MyGenBank.readMyGenBankFile(path);
    }

    // dotplot <name1> <name2>
    // returns Dotplot (Multiline)
    private String createDotPlot(String name1, String name2) throws IOException {
        MyGenBank myGenBank1 = getMyGenBank(name1);
        MyGenBank myGenBank2 = getMyGenBank(name2);
        if (myGenBank1 == null || myGenBank2 == null) {
            return "ERROR: MyGenBank not found.";
        }
        return myGenBank1.getFasta().dotPlot(myGenBank1.getFasta().getDNA(), myGenBank2.getFasta().getDNA());
        
    }

    // embl \n<EMBL>
    // returns MyGenBank (Multiline)
    private MyGenBank EMBLToMyGenBank() throws IOException {
        return MyGenBank.EMBLToMyGenBank(in);
    }

    

    // genbank \n<GenBank>
    // returns MyGenBank (Multiline)
    private MyGenBank GenBankToMyGenBank() throws IOException {
        return MyGenBank.genBankToMyGenBank(in);
    }
}