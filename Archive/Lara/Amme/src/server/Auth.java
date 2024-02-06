package server;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;

public class Auth { //authentifizierung
    private static final String filename = "users.auth";

    // Hilfsfunktionen
    public User[] getUsers() { // Array, weil mehrere User vorhanden sein können
        try {
            return getFromFile();
        } catch (Exception e) {
            return new User[0];
        }
    }

    public User getUser(String username) {
        User[] users = getUsers();
        for (User user : users) { // wird User gefunden?
            if (user.getUsername().equals(username)) {
                return user; // user exists
            }
        }
        return null; // user not exists
    }

    public boolean userExists(String username) {
        return getUser(username) != null;
    }

    public boolean checkPassword(String username, String password) {
        User user = getUser(username);
        if (user == null) {
            return false;
        }
        return user.getPassword().equals(password);
    }

    public boolean addUser(String username, String password) {
        User[] users = getUsers();
        if (userExists(username)) {
            return false;
        }
        User[] newUsers = new User[users.length + 1];

        // copy old array and add new User
        for (int i = 0; i < users.length; i++) {
            newUsers[i] = users[i];
        }
        newUsers[users.length] = new User(username, password);

        // write new array to file
        try {
            writeToFile(newUsers);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return false;
        }
        return true; // user new? -> true
    }

    //save login data
    private void writeToFile(User[] users) throws IOException {
        PrintWriter outputStream = new PrintWriter(new FileOutputStream(filename));
        for(User user : users) {
            outputStream.println(user.getUsername() + ":" + user.getPassword());
        }
        outputStream.close();
    }

    //load login data
    private User[] getFromFile() throws IOException {
        Path path = Paths.get(filename);
        String content = Files.readString(path);
        String[] lines = content.split("\n");
        User[] users = new User[lines.length];
        for (int i = 0; i < lines.length; i++) {
            String[] parts = lines[i].split(":");
            users[i] = new User(parts[0], parts[1]);
        }
        return users;
    }
}