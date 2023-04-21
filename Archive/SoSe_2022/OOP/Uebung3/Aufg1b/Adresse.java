class Adresse {
    String strasse;
    String plz;
    String ort;

    Adresse(String strasse, String plz, String ort) {
        this.strasse = strasse;
        this.plz = plz;
        this.ort = ort;
    }

    String getStrasse() {
        return strasse;
    }

    String getPlz() {
        return plz;
    }

    String getOrt() {
        return ort;
    }
}
