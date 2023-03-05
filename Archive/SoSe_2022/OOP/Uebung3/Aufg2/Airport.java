class Airport {
    Flight[] flights;

    Airport(int maxFlights) {
        this.flights = new Flight[maxFlights];
    }

    void addNewFlight(Flight flight) {
        //Fehlermeldung wenn Flugnummer schon vorhanden
        for (int i = 0; i < flights.length; i++) {
            if (flights[i] != null && flights[i].flightNumber == flight.flightNumber) {
                System.out.println("Flugnummer schon vorhanden");
                return;
            }
        }
        for (int i = 0; i < flights.length; i++) {
            if (flights[i] == null) {
                flights[i] = flight;
                return;
            }
        }
        //Fehlermeldung wenn kein freier Platz vorhanden
        System.out.println("Kein freier Platz vorhanden");
    }

    void removeFlight(int flightNumber){
        for (int i = 0; i < flights.length; i++) {
            if (flights[i] != null && flights[i].flightNumber == flightNumber) {
                flights[i] = null;
                return;
            }
        }
        System.out.println("Flugnummer nicht vorhanden");
    }

    void listDeparturesOnScreen(){
        for (int i = 0; i < flights.length; i++) {
            if (flights[i] != null && flights[i].inOut == false) {
                System.out.println(flights[i].flightNumber + " " + flights[i].time + " " + flights[i].gate + " " + flights[i].location);
            }
        }
    }

    void listArrivalsOnScreen(){
        for (int i = 0; i < flights.length; i++) {
            if (flights[i] != null && flights[i].inOut == true) {
                System.out.println(flights[i].flightNumber + " " + flights[i].time + " " + flights[i].gate + " " + flights[i].location);
            }
        }
    }
}
