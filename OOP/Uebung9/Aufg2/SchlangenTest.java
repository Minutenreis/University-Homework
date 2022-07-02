public class SchlangenTest {
    public static void main(String[] args) {
        Schlange<Integer> schlange1 = new Schlange<Integer>();
        Schlange<String> schlange2 = new Schlange<String>();
        schlange1.push(3);
        schlange1.push(4);
        schlange2.push("a");
        schlange2.push("b");
        schlange1.print();
        schlange2.print();
        WSchlange wschlange = new WSchlange();
        wschlange.push(schlange1.pop());
        wschlange.push(schlange2.pop());
        wschlange.print();
        schlange1.print();
        schlange2.print();
        System.out.println(wschlange.pop());
    }
}
