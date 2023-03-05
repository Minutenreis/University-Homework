
public class RectangleTest {
    public static void main(String[] args) {
            Rectangle r0 = new Rectangle(0, 0, 10, 10){
                @Override
                float getWidth() {
                    return 10;
                }
            };
            Rectangle r1 = new Rectangle(0, 0, 10, 10);
            Rectangle r2 = new Rectangle(0, 0, 10, 20);
            Rectangle r3 = new Rectangle(0, -10, 10, 10);
            Rectangle r4 = new Rectangle(-20, -20, 10, 10);
            Rectangle r5 = new Rectangle(-5, -5, 10, 10);
            //r0 same as r1
            //r1 contained in r2
            //r3 aligned with r1 and r2
            //r4 disjoint to r1 and r2
            //r5 other with r1 and r2

            System.out.println("r0 and r1: "+r0.relativePosition(r1));
            r0.move(0, -5);
            System.out.println("down moved r0 and r1: "+r0.relativePosition(r1));
            r0.move(-10, -10);
            System.out.println("down moved r0 and r1(corner): "+r0.relativePosition(r1));
            System.out.println("r1 and r2: "+r1.relativePosition(r2));
            System.out.println("r3 and r1: "+r3.relativePosition(r1));
            System.out.println("r3 and r2: "+r3.relativePosition(r2));
            System.out.println("r4 and r1: "+r4.relativePosition(r1));
            System.out.println("r4 and r2: "+r4.relativePosition(r2));
            System.out.println("r5 and r1: "+r5.relativePosition(r1));
            r4.move(0,0);
            System.out.println("moved r4 and r1: "+r4.relativePosition(r1));
            r4.decrease(2);
            System.out.println("decreased r4 and r1: "+r4.relativePosition(r1));
            r4.increase(2);
            System.out.println("increased r4 and r1: "+r4.relativePosition(r1));
            r4.move(1,1);
            r4.decrease(2);
            System.out.println("moved and decreased r4 and r1: "+r4.relativePosition(r1));
            System.out.println("same thing but other way around: "+r1.relativePosition(r4));
            Rectangle[] arr = {r0, r1, r2, r3, r4, r5};
            for (Rectangle elem : arr){
                elem.print();}
    }
}
