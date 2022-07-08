import java.util.LinkedList;

public class Schlange<T> {
    LinkedList<T> elementList;

    public Schlange() {
        elementList = new LinkedList<T>();
    }

    public void enqueue(T e) {
        elementList.add(e);
    }

    public T dequeue() {
        return elementList.removeFirst();
    }

    public void print() {
        for (T e : elementList) {
            System.out.print(e+" ");
        }
        System.out.println();
    }
}
