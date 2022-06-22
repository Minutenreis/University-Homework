public class Test {

    /**
     * Methode 1
     */
    static int add(long a, int b) {
        return (int) (a + b);
    } // Methode 1

    /**
     * Methode 2
     */
    static int add(double a, float b) {
        return (int) (a + b);
    } // Methode 2

    /**
     * Methode 3
     */
    static void print(B b, C c) {
    } // Methode 3

    /**
     * Methode 4
     */
    static void print(A a, B b) {
    } // Methode 4

    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        C c = new C();
        // add(1.0, 2.0); // Aufruf 1
        add(1, 2); // Aufruf 2
        add(2, 1L); // Aufruf 3
        print(c, c); // Aufruf 4
        print(a, c); // Aufruf 5
        print(c, b); // Aufruf 6
        // print(b, a); // Aufruf 7

        Print1 p1 = new Print1();
        Print2 p2 = new Print2();
        p1 = p2;
        System.out.print("Aufruf 1 ");
        System.out.println(p1.getX()); // Aufruf 1
        System.out.print("Aufruf 2 ");
        p1.print(c); // Aufruf 2
        System.out.print("Aufruf 3 ");
        ((Print2) p1).print(c); // Aufruf 3
        System.out.print("Aufruf 4 ");
        ((Print1) p2).print(b); // Aufruf 4
        System.out.print("Aufruf 5 ");
        ((Print1) p2).print(c); // Aufruf 5
        System.out.print("Aufruf 6 ");
        p2.print(c); // Aufruf 6
        p1 = new Print1();
        System.out.print("Aufruf 7 ");
        ((Print2) p1).print(a); // Aufruf 7

    }
}
