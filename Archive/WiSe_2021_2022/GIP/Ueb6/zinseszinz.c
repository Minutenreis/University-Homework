#include <stdio.h>

int main()
{
    double kapital, zinssatz, laufzeit;
    printf("\nStartkapital in Euro: ");
    scanf("%lf", &kapital);
    printf("\nZinssatz in Prozent: ");
    scanf("%lf", &zinssatz);
    zinssatz = zinssatz/100 + 1;
    printf("\nGesamtlaufzeit in Jahren: ");
    scanf("%lf", &laufzeit);
    printf("Startkapital = %.2lf\n", kapital);
    for (int i = 1; i <= laufzeit; i++)
    {
        kapital = kapital * zinssatz;
        printf("Jahr: %d\t Kapital: %.2lf Euro\n",i, kapital);
    }
    return 0;
}