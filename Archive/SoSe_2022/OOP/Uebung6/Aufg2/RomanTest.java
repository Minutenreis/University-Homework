public class RomanTest {
    public static void main(String[] args) {
        Roman r1 = new Roman("XCVII");
        Roman r2 = new Roman("XCIX");
        Roman r3 = new Roman("CMXCIX");
        Roman r4 = new Roman("DCCLXXXVII");
        Roman r5 = new Roman(99);
        Roman r6 = new Roman(113);
        Roman r7 = new Roman(512);
        Roman r8 = new Roman(1024);
        Roman[] arr = { r1, r2, r3, r4, r5, r6, r7, r8 };
        System.out.println("number\tarabic\troman\thashcode");
        for (int i = 0; i < arr.length; i++) {
            System.out.println("r"+(i+1)+"\t"+arr[i]+"\t"+arr[i].hashCode());
        }
        System.out.println();
        System.out.println("r1 + r2 = " + r1.add(r2));
        System.out.println("r1 - r2 = " + r1.subtract(r2));
        System.out.println("r6 - r5 = " + r6.subtract(r5));
        System.out.println("r1 * r2 = " + r1.multiply(r2));
        System.out.println("r1 / r2 = " + r1.divide(r2));
        System.out.println("r8 / r5 = " + r8.divide(r5));
        System.out.println("r8 equals r5: " + r8.equals(r5));
        System.out.println("r5 equals r2: " + r5.equals(r2));
    }
}
