public class DreieckigeFliesen extends Fliesen {
    private double seiteA;
    private double seiteB;
    private double seiteC;

    public DreieckigeFliesen(double seiteA, double seiteB, double seiteC) {
        this.seiteA = seiteA;
        this.seiteB = seiteB;
        this.seiteC = seiteC;
    }

    @Override
    public double getFlaecheninhalt() {
        double s = (seiteA + seiteB + seiteC) / 2;
        return Math.sqrt(s * (s - seiteA) * (s - seiteB) * (s - seiteC));
    }

}
