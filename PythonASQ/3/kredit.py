from datetime import date

kredit = int(input("Kredit in Euro: "))
zinssatz = int(input("Zinssatz (Prozent pro Jahr): "))
rueckzahlung = int(input("Jährliche Rückzahlung in Euro: "))
year = date.today().year

while kredit > 0:
    zinsen = kredit * zinssatz // 100
    tilgung = rueckzahlung - zinsen
    rest = kredit - tilgung
    if tilgung < 0:
        exit("Kredit kann nicht zurückgezahlt werden")
    if rest < 0:
        print("Restforderung:", kredit, "EUR")
    else:
        print(year, "Zinsen:", zinsen, "EUR", "Tilgung:", tilgung, "EUR", "Rest:", rest, "EUR")
    kredit = rest
    year += 1
