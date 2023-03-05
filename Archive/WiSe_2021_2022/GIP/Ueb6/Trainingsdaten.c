#include <stdio.h>
#include <math.h>

int main()
{
    double sprungWeite, groessteWeite, zweitGroessteWeite, kleinsteWeite, mittlereWeite, differenz, gesamtweite;
    int anzahlSpruenge;
    groessteWeite = 0;
    zweitGroessteWeite = 0;
    kleinsteWeite = 0;
    gesamtweite = 0;
    anzahlSpruenge = 0;
    printf("Sprungweite [m]: ");
    scanf("%lf", &sprungWeite);
    while (sprungWeite>0)
    {
        if (sprungWeite < kleinsteWeite || kleinsteWeite == 0)
        {
            kleinsteWeite = sprungWeite;
        }

        if (sprungWeite > groessteWeite)
        {
            zweitGroessteWeite = groessteWeite;
            groessteWeite = sprungWeite;
        }
        else if (sprungWeite > zweitGroessteWeite)
        {
            zweitGroessteWeite = sprungWeite;
        }

        gesamtweite += sprungWeite;
        anzahlSpruenge++;
        printf("Sprungweite [m]: ");
        scanf("%lf", &sprungWeite);
    }
    mittlereWeite = gesamtweite / ((double)anzahlSpruenge);
    differenz = groessteWeite - kleinsteWeite;
    printf("\n\nAnzahl der Spruenge: \t%d\n", anzahlSpruenge);
    printf("weitester Sprung: \t%.2lf m\n", groessteWeite);
    printf("zweitweitester Sprung: \t%.2lf m\n", zweitGroessteWeite);
    printf("kuerzester Sprung: \t%.2lf m\n", kleinsteWeite);
    printf("mittlere Weite: \t%.2lf m\n", mittlereWeite);
    printf("Differenz Sprungweiten:\t%.2lf m\n", differenz);
}