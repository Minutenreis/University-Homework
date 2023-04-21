public class RundeFliesen extends Fliesen {
    double radius;

    RundeFliesen(double radius){
        this.radius = radius;
    }
    @Override
    double getFlaecheninhalt() {
        return radius * radius * 3.14;
    }
}
