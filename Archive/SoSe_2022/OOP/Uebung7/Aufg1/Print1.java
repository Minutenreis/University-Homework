public class Print1 {
    int x = 1;

    public int getX() {
        return x;
    }

    public int getXPrint1() {
        return x;
    }

    public void print(A a) {
        System.out.print("Print 1 A x=" + x + " ");
        System.out.println(x);
    }

    public void print(B b) {
        System.out.print("Print1 B x=" + x + " ");
        System.out.println(x + 1);
    }
}
