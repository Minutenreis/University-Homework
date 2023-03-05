#include <stdio.h>
#include <math.h>

int main()
{
    int isHappy();
    for (int i = 1; i <= 500; i++)
    {
        if (isHappy(i))
        {
            printf("%d\n", i);
        }
    }
    return 0;
}

int isHappy(int number)
{
    int perfectDigitalInvariant();
    while (number > 1 && number != 20) //wenn unhappyNumber wird 20 immer in der Wiederholung auftauchen
    {
        number = perfectDigitalInvariant(number);
    }
    return (number == 1);
}

int perfectDigitalInvariant(int i)
{
    int result = 0;
    while (i > 0)
    {
        result += (i % 10) * (i % 10); //Quadrat letzter Ziffer hinzuaddieren
        i /= 10;                       //letzte Ziffer entfernen und Zahl eins nach rechts ruecken
    }
    return result;
}