#include <stdio.h>
int anzahlZiffer(int n, int digit);

int main()
{
    int number;
    int digit;
    printf("Geben Sie ihre Zahl ein: \n");
    scanf("%d", &number);
    if (number < 0)
    {
        printf("Ungueltige Eingabe");
        return 0;
    }
    printf("Nach welcher Ziffer wollen sie suchen?\n");
    scanf("%d", &digit);
    if (digit < 0 || digit >= 10)
    {
        printf("Ungueltige Eingabe");
        return 0;
    }
    printf("Es gibt %d %den in %d\n", anzahlZiffer(number, digit), digit, number);
    return 0;
}

int anzahlZiffer(int n, int digit)
{
    if (n > 0)
    {
        if (n % 10 == digit)
        {
            return 1 + anzahlZiffer(n / 10, digit);
        }
        return anzahlZiffer(n / 10, digit);
    }
    return 0;
}