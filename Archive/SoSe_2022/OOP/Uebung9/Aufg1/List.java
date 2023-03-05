public class List {
    private Node head;

    public List() {
        head = null;
    }

    public List(Object e) {
        head = new Node(e);
    }

    public void add(Object e) {
        Node newNode = new Node(e);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    public void remove(Node e){
        if (head == null) {
            return; // Liste ist leer
        } else if (head.next == null) {
            head = null; //e == head => einziges Element
        } else { //e != head => mehrere Elemente
            Node current = head;
            while (current.next != e) { //e suchen
                current = current.next;
            } //current ist vorheriges Element
            current.next = current.next.next;
        }
    }

    public void traverseAndApply(ActionObject p) {
        for (Node cursor = head; cursor != null; cursor = cursor.next) {
            p.action(cursor);
        }
    }

}
