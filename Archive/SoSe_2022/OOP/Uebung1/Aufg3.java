import java.util.Scanner;

public class Aufg3 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Wie viele Gäste sind auf der Party? ");
        int number = reader.nextInt();
        reader.close();
        System.out.println("rekursiv:" + prost(number));
    }

    static int prost(int n) {
        if (n <= 1) {
            return 0;
        }
        return prost(n - 1) + n - 1;
    }
}
