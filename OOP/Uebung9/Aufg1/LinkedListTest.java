public class LinkedListTest {
    public static void main(String[] args) {
        List list = new List(3);
        list.add(4);
        list.add('e');
        list.add("satz");
        list.add(new List(5));
        list.add(new Node(new List(4)));
        showContainsZero(list);
        showPosSum(list);
        list.add(0);
        list.add(5);
        list.add(-3);
        showContainsZero(list);
        showPosSum(list);
    }

    static public void showContainsZero(List list) {
        ContainsZeroActionObject containsZeroAO = new ContainsZeroActionObject();
        list.traverseAndApply(containsZeroAO);
        System.out.println("ContainsZero: " + containsZeroAO.containsZero());
    }

    static public void showPosSum(List list){
        PosSumActionObject posSumAO = new PosSumActionObject();
        list.traverseAndApply(posSumAO);
        System.out.println("PosSum: " + posSumAO.getSum());
    }
}
