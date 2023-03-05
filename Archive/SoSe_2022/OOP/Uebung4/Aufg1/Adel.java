class Adel extends Einwohner {

    Adel(int einkommen) {
        super(einkommen);
    }

    @Override
    int steuer() {
        if (grundSteuer() < 20){
            return 20;
        }
        return grundSteuer();
    }

}
