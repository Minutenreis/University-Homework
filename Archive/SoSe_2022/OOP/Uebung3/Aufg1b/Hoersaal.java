class Hoersaal {
    Integer plaetze;
    Vorlesung[] vorlesungen;
    Adresse adresse;

    Hoersaal(Integer plaetze, Adresse adr, Vorlesung[] vlg) {
        this.adresse = adr;
        this.plaetze = plaetze;
        this.vorlesungen = vlg;
    }

    Integer getPlaetze() {
        return plaetze;
    }

    Vorlesung[] getVorlesungen() {
        return vorlesungen;
    }

    Adresse getAdresse() {
        return adresse;
    }
    
}
