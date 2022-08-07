public class Auftragsabwicklung {
    public static void main(String args[]) {
        final double produktion = 200; // Wochenproduktion
        // f¨ulle die Bestellung mit Fl¨ussigkeitsbeh¨altnissen
        Behaeltnis[] bestellung = {
                new Tetrapack(2.3, 0.9, 0.7),
                new Dose(0.59, 1.15),
                new Dose(0.59, 1.15), 
                new Tetrapack(1.1, 0.7, 0.7) // ...
        };
        // gebe Liste aller bestellten Fl¨ussigkeitsbeh¨altnisse aus
        for (int i = 0; i < bestellung.length; i++) {
            bestellung[i].println();
        }
        // berechne das Gesamtvolumen der Bestellung
        // und die Restmenge der Wochenproduktion
        // >>> Diesen Programmteil sollen Sie hier erg¨anzen! <<<
        double gesamtvolumen = 0;
        for(Behaeltnis behaeltnis: bestellung) {
            gesamtvolumen += behaeltnis.volumen();
        }
        double restmenge = produktion - gesamtvolumen;
        System.out.println("Gesamtvolumen: " +String.format("%.2f",gesamtvolumen));
        System.out.println("Restmenge: " + String.format("%.2f",restmenge));
        if(restmenge < 0){
            System.out.println("Die Wochenproduktion ist zu gering!");
        } 
    }
}
