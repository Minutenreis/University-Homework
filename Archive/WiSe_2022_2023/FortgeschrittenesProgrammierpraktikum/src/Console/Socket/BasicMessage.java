package Console.Socket;

public class BasicMessage {
    private final String body;
    private final String subject;
    private final String from;
    private final String[] to;

    protected BasicMessage(String body, String subject, String from, String[] to) {
        this.body = body;
        this.subject = subject;
        this.from = from;
        this.to = to;
    }

    public String getBody() {
        return body;
    }

    public String getSubject() {
        return subject;
    }

    public String getFrom() {
        return from;
    }

    public String[] getTo() {
        return to;
    }

    public String getToString() {
        return String.join(",", to);
    }
}
