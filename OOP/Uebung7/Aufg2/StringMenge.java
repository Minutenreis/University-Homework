interface StringMenge {
    /**
     * fügt den übergebenen String der Menge hinzu, wenn er noch nicht darin vorkommt
     **/
    void add(String s);

    /**
     * entfernt den ubergebenen String aus der Menge, wenn er vorhanden ist
     */
    void remove(String s);

    /**
     * gibt true zuruck, wenn der übergebene String in der Menge ist, ansonsten false
     */
    boolean contains(String s);

     /**
      * gibt true zurück, wenn die Menge leer ist, ansonsten false
     */
    boolean isEmpty();

     /**
      * gibt die Anzahl der Strings in der Menge zurück
     */
    int getSize();

     /**
      * liefert ein StringArray zurück, welches alle Strings der Menge enthält
     */
    String[] getElements();

     /**
      * liefert die Anzahl der Zeichen in der Menge zurück
     */
    int getCharCount();

     /**
      * gibt die Elemente der Menge am Bildschirm aus
     */
    void print();
}
