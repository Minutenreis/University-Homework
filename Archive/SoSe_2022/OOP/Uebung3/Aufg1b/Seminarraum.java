class Seminarraum{
    Integer plaetze;
    Uebung[] uebungen;
    Adresse adresse;

    Seminarraum(Integer plaetze, Adresse adr, Uebung[] ueb) {
        this.adresse = adr;
        this.plaetze = plaetze;
        this.uebungen = ueb;
    }

    Integer getPlaetze() {
        return plaetze;
    }

    Uebung[] getUebungen() {
        return uebungen;
    }

    Adresse getAdresse() {
        return adresse;
    }
}
