public class Main {
    
    public static void main(String[] args) {
        Article book = new Book();
        System.out.println(book.zeichenzahl()); //1
        System.out.println(book.woerter()); //2
        // System.out.println(book.seitenzahl()); // Compile Error
        System.out.println(book.woerter); //1
    }
}
