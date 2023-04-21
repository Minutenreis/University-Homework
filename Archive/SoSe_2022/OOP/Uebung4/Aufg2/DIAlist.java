class DIAlist extends DynIntArray{
    Node head;
    Node tail;

    class Node {
        int value;
        Node next;
        Node prev;  

        Node(int value) {
            this.value = value;
            this.next = null;
            this.prev = null;
        }
    }

    DIAlist() {
        super();
        head = null;
        tail = null;
    }

    @Override
    int getElementCount() {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    @Override
    int getElementAt(int i) {
        if (i < 0 || i >= getElementCount()) {
            return 0;
        }
        Node current = head;
        for (int j = 0; j < i; j++) {
            current = current.next;
        }
        return current.value;
    }

    @Override
    void setElementAt(int i, int e) {
        if (i < 0 || i >= getElementCount()) {
            return;
        }
        Node current = head;
        for (int j = 0; j < i; j++) {
            current = current.next;
        }
        current.value = e;
    }

    @Override
    void add(int e) {
        Node newNode = new Node(e);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
    }

    @Override
    void print() {
        Node current = head;
        System.out.print("[");
        while (current != null) {
            if(current != head){
                System.out.print(", ");
            }
            System.out.print(current.value);
            current = current.next;
        }
        System.out.println("]");
    }
}
