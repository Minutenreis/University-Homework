public class Node <T>{
    private T data;
    private Node<T> next;
    private Node<T> prev;
    private Node(T data) {
        this.data = data;
    }
    public T getData() {
        return this.data;
    }
    public Node<T> getNext() {
        return this.next;
    }
    public Node<T> getPrev() {
        return this.prev;
    }
    public void setNext(Node<T> next) {
        this.next = next;
    }
    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }
}
