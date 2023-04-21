import java.util.ArrayList;
import java.util.List;

public class BinarySearch {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < 100; i++) {
            list.add(i);
        }
        int key = 30;
        System.out.println(binarySearchIt(list, key));
        System.out.println(binarySearchRec(list, key));
    }

    public static int binarySearchIt(ArrayList<Integer> list, int key) {
        int low = 0;
        int high = list.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (key < list.get(mid)) {
                high = mid - 1;
            } else if (key > list.get(mid)) {
                low = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    public static int binarySearchRec(List<Integer> list, int key) {
        int mid = list.size() / 2;
        if (key < list.get(mid)) {
            return binarySearchRec(list.subList(0, mid), key);
        } else if (key > list.get(mid)) {
            return binarySearchRec(list.subList(mid + 1, list.size()), key) + mid + 1;
        } else {
            return mid;
        }
    }
}
