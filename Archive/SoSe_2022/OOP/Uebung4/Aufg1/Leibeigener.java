class Leibeigener extends Bauer {
    
    Leibeigener(int einkommen) {
        super(einkommen);
    }
    
    @Override
    int zuVersteuerndesEinkommen() {
        int steuerpflichtigesEinkommen = einkommen - 12;
        if (steuerpflichtigesEinkommen < 0) {
            steuerpflichtigesEinkommen = 0;
        }
        return steuerpflichtigesEinkommen;
    }
}
