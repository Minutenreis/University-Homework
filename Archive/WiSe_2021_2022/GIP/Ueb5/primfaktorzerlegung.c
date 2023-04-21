#include <stdio.h>

int main()
{
    int number;
    printf("Bitte geben sie eine Zahl ein: ");
    scanf("%d", &number);
    if (number < 2)
    {
        printf("Ungueltige Eingabe");
        return 0;
    }
    int factor = 2;                     //erste Primzahl
    printf("Faktoren: \n");
    while (number > 1)
    {
        if (number % factor == 0)       //Zahl durch Faktor teilbar?
        {
            printf("%d\n", factor);
            number = number / factor;   //Rest ausrechnen
        } else {
            factor++;                   //naechsthoehere Zahl ausprobieren => es wird immer erst durch eine Primzahl teilbar sein
        }
    }
    return 0;
}