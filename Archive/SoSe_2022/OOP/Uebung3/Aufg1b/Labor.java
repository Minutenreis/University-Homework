class Labor{
    Integer plaetze;
    Praktikum[] praktika;
    Adresse adresse;

    Labor(Integer plaetze, Adresse adr, Praktikum[] prk) {
        this.adresse = adr;
        this.plaetze = plaetze;
        this.praktika = prk;
    }

    Integer getPlaetze() {
        return plaetze;
    }

    Praktikum[] getPraktika() {
        return praktika;
    }

    Adresse getAdresse() {
        return adresse;
    }
}
