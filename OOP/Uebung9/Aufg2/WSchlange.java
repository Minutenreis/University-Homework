import java.util.LinkedList;

public class WSchlange {
    LinkedList<Object> elementList;

    public WSchlange() {
        elementList = new LinkedList<Object>();
    }

    public void push(Object e) {
        elementList.add(e);
    }

    public Object pop() {
        return elementList.removeFirst();
    }

    public void print() {
        for (Object e : elementList) {
            System.out.print(e + " ");
        }
        System.out.println();
    }
}
