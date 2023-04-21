#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main()
{
    double accuracy, pi, lastPi, divisor, absoluteError, relativeError;
    int digits, factorPlusMinus, counter;
    printf("Geben sie eine Genauigkeit an: ");
    scanf("%lf", &accuracy);
    digits = -log10(accuracy)+2;    //wichtige Nachkommastellen approximieren
    counter = 0;
    pi = 0;
    lastPi = 0;            
    factorPlusMinus = 1;    //erst wird addiert
    divisor = 1;            //erst wird durch 1 geteilt
    if (accuracy <= 0)
    {
        printf("ungueltige Eingabe");
        return 0;
    }

    do
    {
        lastPi = pi;
        pi += factorPlusMinus * 4 / divisor;
        factorPlusMinus = factorPlusMinus * (-1);
        divisor += 2;
        counter++;
    }
    while (fabs(pi - lastPi) >= accuracy);
    absoluteError = fabs(pi - M_PI);
    relativeError = fabs(pi / M_PI - 1);

    printf("Pi: %.*lf\n", digits, pi);
    printf("Pi hat einen absoluten Fehler von %.2e und einen relativen Fehler von %.2e Prozent.\n", absoluteError, relativeError * 100);
    printf("Iterationen: %d\n", counter);
}