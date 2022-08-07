public class SchlangenTest {
    public static void main(String[] args) {
        Schlange<Integer> schlange1 = new Schlange<Integer>();
        Schlange<String> schlange2 = new Schlange<String>();
        schlange1.enqueue(3);
        schlange1.enqueue(4);
        schlange2.enqueue("a");
        schlange2.enqueue("b");
        schlange1.print();
        schlange2.print();
        WSchlange wschlange = new WSchlange();
        wschlange.enqueue(schlange1.dequeue());
        wschlange.enqueue(schlange2.dequeue());
        wschlange.print();
        schlange1.print();
        schlange2.print();
        System.out.println(wschlange.dequeue());
    }
}
