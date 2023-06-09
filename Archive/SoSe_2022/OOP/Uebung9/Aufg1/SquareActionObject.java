public class SquareActionObject implements ActionObject {
    public void action(Node n) {
        if (n.data instanceof Number) {
            n.data = Math.pow(((Number) n.data).doubleValue(), 2);
        }
    }
}
