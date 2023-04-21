import java.util.Arrays;

public class Aufg1 {

    public static void main(String[] args) {
        int[] a1 = { 1, 2, 3, 4, 5 };
        int[] c = AufgC(a1);
        int[] d = AufgD(a1);
        System.out.println(Arrays.toString(c));
        System.out.println(Arrays.toString(d));
    }

    public static int[] AufgC(int[] a) {
        int[] a1 = new int[a.length % 2 == 1 ? a.length / 2 + 1 : a.length / 2];
        int[] a2 = new int[a.length/2];
        for (int i = 0; i < a.length; i++) {
            if (i % 2 == 0) {
                a1[i / 2] = a[i];
            } else {
                a2[i / 2] = a[i];
            }
        }
        return a1;
    }

    public static int[] AufgD(int[] a) {
        int evenElements = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] % 2 == 0) {
                evenElements++;
            }
        }
        int[] b1 = new int[evenElements];
        int[] b2 = new int[a.length - evenElements];
        int j = 0;
        int k = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] % 2 == 0) {
                b1[j] = a[i];
                j++;
            } else {
                b2[k] = a[i];
                k++;
            }
        }
        return b1;
    }

}
