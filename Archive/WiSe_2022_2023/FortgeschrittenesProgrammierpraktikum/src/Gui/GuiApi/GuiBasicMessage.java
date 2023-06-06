package GuiApi;

public class GuiBasicMessage {
    public final String body;
    public final String subject;
    public final String from;
    public final String to;
    public final String cc;

    public GuiBasicMessage(String body, String subject, String from, String to, String cc) {
        this.body = body;
        this.subject = subject;
        this.from = from;
        this.to = to;
        this.cc = cc;
    }

    public String getToString() {
        return String.join(",", to);
    }

    public boolean isValid(){
        return body != null && subject != null && from != null && to != null;
    }
}
