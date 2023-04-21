class Einwohner {
    int einkommen;

    Einwohner(int einkommen) {
        this.einkommen = einkommen;
    }

    void setEinkommen(int einkommen){
        this.einkommen = einkommen;
    }

    protected int grundSteuer() {
        int steuer = (int) (zuVersteuerndesEinkommen()*0.1);
        if (steuer < 1) {
            steuer = 1;
        }
        return steuer;
    }

    int steuer(){
        return grundSteuer();
    }

    int zuVersteuerndesEinkommen(){
        return einkommen;
    }
}
