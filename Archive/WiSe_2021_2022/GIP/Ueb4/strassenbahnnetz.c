#include <stdio.h>
#include <stdlib.h>

int start, ziel, sLinie, sStation, eLinie, eStation;

int main()
{
    int preis;
    int startpreis(), endhaltestellen(), ungueltig(), zonenuebergaenge(), noDistance(), startKleiner(), trennenInStationUndLinie();
    printf("Starthaltestelle: ");
    scanf("%d", &start);
    printf("Zielhaltestelle: ");
    scanf("%d", &ziel);
    startKleiner();
    trennenInStationUndLinie();
    if (ungueltig())
    {
        printf("Ungueltige Eingabe");
        return 0;
    }
    if (noDistance())
    {
        printf("Run Bitch");
        return 0;
    }
    preis = startpreis() + endhaltestellen() + zonenuebergaenge();
    printf("%d\n", startpreis());
    printf("%d\n", endhaltestellen());
    printf("%d\n", zonenuebergaenge());
    printf("%d Euro", preis);
    return 0;
}

int ungueltig()
{
    if (sLinie < 0 || sLinie > 5 || eLinie < 0 || eLinie > 5 || sStation < 0 || sStation > 5 || eStation < 0 || eStation > 5)
    { //Eingabe Grob out of Bounds
        return 1;
    }
    if ((sLinie == 0 || sStation == 0) && (start != 0) || (eLinie == 0 || eStation == 0) && (ziel != 0))
    { //Eingabe beinhaltet 0, ist aber nicht 00 (Mitte)
        return 1;
    }
    return 0;
}

int startpreis()
{
    if ((sLinie == eLinie || sLinie == 0) && (abs(sStation - eStation) == 1) && !(start == 0 && ziel == 21))
    { //Abfrage benachbart auf einer Linie
        return 2;
    }
    else if ((sStation == 2 && eStation == 2) && (abs(eLinie - sLinie) == 1 || sLinie == 1 && eLinie == 5) && !(sLinie == 4 && eLinie == 5))
    { //Abfrage benachbart in Ring
        return 2;
    }
    else
    { //keine Sonderfälle
        return 3;
    }
}

int endhaltestellen()
{
    if (sStation == 5)
    { //Start auf Endhaltestelle
        return 1;
    }
    else if (eStation == 5)
    { //Ziel auf Endhaltestelle
        return 1;
    }
    else
    {
        return 0;
    }
}

int zonenuebergaenge()
{
    if ((sStation > 2 && eStation <= 2) || (sStation <= 2 && eStation > 2))
    { //ein Uebergang
        return 1;
    }
    else if (sStation > 2 && eStation > 2 && sLinie != eLinie)
    { //beide Ausserhalb auf verschiedenen Strecken => 2 Zonenuebergaenge
        return 2;
    }
    else
    {
        return 0;
    }
}

int noDistance()
{
    if (start == ziel)
    { //fährt auf gleiches Feld
        return 1;
    }
    else
    {
        return 0;
    }
}

int startKleiner()
{
    int temp;
    if (start > ziel)
    {
        temp = start;
        start = ziel;
        ziel = temp;
    }
}

int trennenInStationUndLinie()
{
    sLinie = start / 10;
    sStation = start % 10;
    eLinie = ziel / 10;
    eStation = ziel % 10;
}