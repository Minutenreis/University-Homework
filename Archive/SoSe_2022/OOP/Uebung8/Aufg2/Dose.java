public class Dose extends Behaeltnis {
    double radius, hoehe;

    public Dose(double radius, double hoehe) {
        if(radius < 0 || hoehe < 0) {
            throw new IllegalArgumentException("Radius und Hoehe müssen positiv sein!");
        }
        this.radius = radius;
        this.hoehe = hoehe;
    }

    @Override
    public void println() {
        System.out.println("Dose mit Flaeche " + String.format("%.2f",radius*radius*Math.PI) + " und Hoehe " + hoehe);
    }

    @Override
    public double volumen() {
        return Math.PI * radius * radius * hoehe;
    }
}
