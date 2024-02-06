package server;

public class User{
    public String username;
    public String password;

    User(String username, String password){
        this.username = username;
        this.password = password;
    }

    public String getUsername(){
        return this.username;
    }

    public String getPassword(){
        return this.password;
    }

    public String toString(){
        return this.username + " " + this.password;
    }
}