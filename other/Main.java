public class Main {
    public static <T extends Comparable<T>> T findMaxG(T[] array) {
        T max = array[0];
        for (int i = 0; i < array.length; i++) {
            if (array[i].compareTo(max) > 0) {
                max = array[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        String[] array = { "\n" };
        System.out.println(findMaxG(array));
    }
}
