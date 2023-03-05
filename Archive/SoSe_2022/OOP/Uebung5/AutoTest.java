public class AutoTest {
    public static void main(String[] args) {
        Auto[] autos = new Auto[7];
        autos[0] = new Auto();
        autos[1] = new Auto("J-AA 02");
        autos[2] = new Auto("J-AA 03", Auto.AnzahlPlaetze.ZWEI);
        autos[3] = new Auto(Auto.AnzahlPlaetze.FUENF);
        autos[4] = new Auto("J-AA 04", Auto.AnzahlPlaetze.FUENF);
        autos[5] = new PickUp(100);
        autos[6] = new PickUp("J-AA 05", 100);
        autosToString(autos);
        for (int i = 0; i < autos.length; i++) {
            autos[i].fahreAntenneAus();
            autos[i].fahreAntenneAus();
            autos[i].fahre(10*i);
            autos[i].fahreAntenneEin();
            autos[i].getKilometerstand();
            autos[i].getSitzplaetze();
            autos[i].getKennzeichen();
            autos[i].fahreAntenneAus();
            if(autos[i] instanceof PickUp){
                PickUp pickup = (PickUp)autos[i];
                pickup.beladen(20*i);
                pickup.entladen(50);
                pickup.entladen();
                pickup.entladen(20);
                pickup.wasche();
            }
        }
        autosToString(autos);
    }

    static void autosToString(Auto[] autos){
        for(int i = 0; i < autos.length; i++){
            System.out.println(autos[i]);
        }
    }
}
