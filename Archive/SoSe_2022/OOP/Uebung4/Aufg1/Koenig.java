class Koenig extends Einwohner{

    Koenig(int einkommen) {
        super(einkommen);
    }

    @Override
    int steuer() {
        return 0;
    }
    
}
