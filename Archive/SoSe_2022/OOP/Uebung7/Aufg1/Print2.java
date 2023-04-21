public class Print2 extends Print1 {
    int x = 3;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getXPrint2() {
        return x;
    }

    public void print(A a) {
        System.out.print("Print 2 A x=" + x + " ");
        System.out.println(x);
    }

    public void print(B b) {
        System.out.print("Print2 B x=" + x + " ");
        System.out.println(x + 1);
    }

    public void print(C c) {
        System.out.print("Print2 C x=" + x + " ");
        System.out.println(x + 2);
    }
}
