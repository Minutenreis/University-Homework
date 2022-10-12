public class Main {
    
    public static void main(String[] args) {
        Article book = new Book(){
            @Override
            int zeichenzahl(){
                return 5;
            }
        };
        
        Article book2 = new Book2();
        Something test = (a,b) -> a+b;
        Something test2 = new Something(){
            public int something(int a, int b){return a+b;};
        };
        System.out.println(test.something(3,4));
        System.out.println(test2.something(4,3));
        System.out.println(book.zeichenzahl()); //5
        System.out.println(book2.zeichenzahl());//5
        System.out.println(book.woerter()); //2
        // System.out.println(book.seitenzahl()); // Compile Error
        System.out.println(book.woerter); //1
    }
}
