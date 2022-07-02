public class List {
    Node head;

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

    public void traverseAndApply(ActionObject p) {
        for (Node cursor = head; cursor != null; cursor = cursor.next) {
            p.action(cursor);
        }
    }

}
