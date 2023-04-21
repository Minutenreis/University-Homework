#include <stdio.h>
#include <math.h>

int main()
{
    int tempC, tempF;
    float tempCFloat;
    printf("Geben Sie eine positive ganzzahlige Temperatur in Grad Fahrenheit ein: ");
    scanf("%d", &tempF);
    tempCFloat = (tempF - 32);
    tempCFloat = tempCFloat * 5 / 9;
    tempC = round(tempCFloat);
    if (tempF >= 0)
    {
        printf("%d Grad Fahrenheit sind %d Grad Celsius ", tempF, tempC);
    }
    else
    {
        printf("Die eingegebene Temperatur ist kleiner als 0");
    }
    return 0;
}