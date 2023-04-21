import java.util.Scanner;

public class Aufg2 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Welches Fibonacci Glied wollen sie haben? ");
        int number = reader.nextInt();
        reader.close();
        if (number < 0) {
            return;
        }
        System.out.println(fibonacci(number));
        return;
    }

    static int fibonacci(int number) {
        int currentNumber = 1, previousNumber = 0;
        if (number == 0) {
            return 0;
        }
        for (int i = 1; i < number; i++) {
            currentNumber = currentNumber + previousNumber;
            previousNumber = currentNumber - previousNumber; // currentNumber - previousNumber = vorherige currentNumber
        }
        return currentNumber;
    }
}
