public class EckigeFliesen extends Fliesen{
    double breite, laenge;

    EckigeFliesen(double breite, double laenge){
        this.breite = breite;
        this.laenge = laenge;
    }
    @Override
    double getFlaecheninhalt() {
        return breite * laenge;
    }
}
