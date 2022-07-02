public class ContainsZeroActionObject implements ActionObject {
    boolean containsZero = false;

    public void action(Node n) {
        if (Integer.class.isInstance(n.data)) {
            if ((int) n.data == 0) {
                containsZero = true;
            }
        }
    }
}