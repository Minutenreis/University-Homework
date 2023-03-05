#include <stdio.h>
#include <math.h>

int main()
{
    int isHappy();
    int i = 1;
    for (i = 1; i <= 500; i++)
    {
        if (isHappy(i))
        {
            printf("%d\n", i);
        }
    }
}

int isHappy(int i)
{
    int perfectDigitalInvariant();
    int result;
    result = perfectDigitalInvariant(i);
    if (result != 1 && result != 20)
    {
        return isHappy(result);
    }
    else
    {
        return (result == 1);
    }
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