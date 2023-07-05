public class LinkedListTest {
    public static void main(String[] args) {
        LinkedListTest main = new LinkedListTest();
        List list = new List(3);
        list.add(4);
        list.add('e');
        list.add("satz");
        list.add(new List(5));
        list.add(new Node(new List(4)));
        main.showContainsZero(list);
        main.showPosSum(list);
        list.add(0);
        list.add(5);
        list.add(-3);
        main.showContainsZero(list);
        main.showPosSum(list);
        main.square(list);
    }

    public void showContainsZero(List list) {
        ContainsZeroActionObject containsZeroAO = new ContainsZeroActionObject();
        list.traverseAndApply(containsZeroAO);
        System.out.println("ContainsZero: " + containsZeroAO.containsZero());
    }

    public void showPosSum(List list) {
        PosSumActionObject posSumAO = new PosSumActionObject();
        list.traverseAndApply(posSumAO);
        System.out.println("PosSum: " + posSumAO.getSum());
    }

    public void square(List list) {
        SquareActionObject squareAO = new SquareActionObject();
        PrintActionObject printAO = new PrintActionObject();
        list.traverseAndApply(printAO);
        list.traverseAndApply(squareAO);
        list.traverseAndApply(printAO);
    }
}
