public class Tetrapack extends Behaeltnis{
    double laenge, breite, hoehe;

    public Tetrapack(double laenge, double breite, double hoehe){
        if(laenge < 0 || breite < 0 || hoehe < 0){
            throw new IllegalArgumentException("Length, Width und Height müssen positiv sein!");
        }
        this.laenge = laenge;
        this.breite = breite;
        this.hoehe = hoehe;
    }

    @Override
    public void println(){
        System.out.println("Tetrapack: mit Kanten " + laenge + ", " + breite + ", " + hoehe);
    }

    @Override
    public double volumen(){
        return laenge * breite * hoehe;
    }
}
