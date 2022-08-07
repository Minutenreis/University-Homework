public class ContainsZeroActionObject implements ActionObject {
    boolean containsZero = false;

    public void action(Node n) {
        if (n.data instanceof Integer && (int) n.data == 0) {
            containsZero = true;
        }
    }
}