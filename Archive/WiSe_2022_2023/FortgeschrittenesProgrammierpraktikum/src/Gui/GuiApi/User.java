package GuiApi;

import java.io.Serializable;

public class User implements Serializable {

    public enum POP3PROTOCOL {
        SSL, NO_SSL
    }

    public enum SMTPPROTOCOL {
        SSL, TLS, NO_SSL
    }
    
    public String username;
    public String password;

    public String pop3Server;
    public Integer pop3Port;
    public POP3PROTOCOL pop3Protocol;

    public String smtpServer;
    public Integer smtpPort;
    public SMTPPROTOCOL smtpProtocol;

    public User() {
        this.pop3Protocol = POP3PROTOCOL.SSL;
        this.smtpProtocol = SMTPPROTOCOL.TLS;
    }
}
