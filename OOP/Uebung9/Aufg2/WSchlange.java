import java.util.LinkedList;

public class WSchlange {
    private LinkedList<Object> elementList;

    public WSchlange() {
        elementList = new LinkedList<Object>();
    }

    public void enqueue(Object e) {
        elementList.add(e);
    }

    public Object dequeue() {
        return elementList.removeFirst();
    }

    public Object peek() {
        return elementList.getFirst();
    }

    public void print() {
        for (Object e : elementList) {
            System.out.print(e + " ");
        }
        System.out.println();
    }
}
