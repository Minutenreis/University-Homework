public class Main {
    public static void main(String[] args) {
        Fliesen eFliese = new EckigeFliesen(3, 4);
        Fliesen rFliese = new RundeFliesen(3);
        System.out.println(eFliese.getFlaecheninhalt());
        System.out.println(rFliese.getFlaecheninhalt());
        System.out.println(eFliese.stuff());
    }
}
