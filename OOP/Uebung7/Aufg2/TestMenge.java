public class TestMenge {
    public static void main(String args[]) {
        java.util.Random rand = new java.util.Random();
        StringMenge sm = new StringMengeImpl();
        while (sm.getSize() < 5) {
            String r = "Eingabe" + String.valueOf(rand.nextInt(5));
            boolean c = sm.contains(r);
            sm.add(r);
            System.out.printf("Element %3s ist %15s, Mengen-Groeße ist %2d, " +
                    "mit: ", r, ((c ? "" : "nicht ") + "vorhanden"), sm.getSize());
            sm.print();
            System.out.print(" Zeichenanzahl= " + sm.getCharCount());
            System.out.println();
        }
    }
}
