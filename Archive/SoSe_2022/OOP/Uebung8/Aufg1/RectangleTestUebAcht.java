public class RectangleTestUebAcht {
    public static void main(String[] args) {
        Rectangle rects[] = new Rectangle[4];
        rects[0] = new Rectangle(0, 0, 10, 10, 0xFF0000);
        rects[1] = new Rectangle(10, 0, 20, 10, 0x00FF00);
        rects[2] = new Rectangle(0, 10, 10, 20, 0x0000FF);
        rects[3] = new Rectangle(10, 10, 40, 40, 0xFFFF00);
        for (int i = 0; i < rects.length; i++) {
            System.out.println(rects[i]);
        }
        resizeAll(30, rects);
        moveAll(20,20, rects);
        for (int i = 0; i < rects.length; i++) {
            System.out.println(rects[i]);
        }
    }

    public static void resizeAll(float r, ResizeableGO rgo[]) {
        for (ResizeableGO g : rgo)
            g.resize(r);
    }

    public static void moveAll(float dx, float dy, MoveableGO mgo[]) {
        for (MoveableGO m : mgo)
            m.move(dx, dy);
    }
}
