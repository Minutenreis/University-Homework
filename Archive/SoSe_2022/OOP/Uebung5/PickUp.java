public class PickUp extends Auto{
    int f;
    int ladung;

    PickUp(int fassungsvermögen){
        super();
        this.sitzplaetze = 2;
        this.f = fassungsvermögen;
        this.ladung = 0;
    }

    PickUp(String kennzeichen, int fassungsvermögen){
        super(kennzeichen, AnzahlPlaetze.ZWEI);
        this.f = fassungsvermögen;
        this.ladung = 0;
    }

    int getLadung(){
        return this.f;
    }

    boolean beladen(int ladung){
        if(this.ladung + ladung > this.f){
            System.out.println("Ladung überschreitet Fassungsvermögen");
            return false;
        } else {
            this.ladung += ladung;
            System.out.println("Auto wurde mit "+ladung+" beladen");
            return true;
        }
    }

    void entladen(int ladung){
        if(this.ladung - ladung <= 0){
            this.ladung = 0;
            System.out.println("Fahrzeug vollständig entladen");
        } else {
            this.ladung -= ladung;
            System.out.println("Auto wurde mit "+ladung+" entladen");
        }
    }

    void entladen(){
        this.entladen(this.ladung);
    }

    void bereiteWaschenVor(){
        this.entladen();
        super.bereiteWaschenVor();
    }

    public String toString(){
        return super.toString() + "\tmit Fassungsvermögen "+this.f+" und Ladung "+this.ladung;
    }
}
