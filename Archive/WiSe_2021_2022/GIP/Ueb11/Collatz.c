#include <stdio.h>
int collatzIterative(int number);
int collatzRekursive(int number);

int main()
{
    int collatzNumber;
    while (1)
    {
        printf("Geben sie eine positive natuerliche Zahl ein: ");
        scanf("%d", &collatzNumber);
        if (collatzNumber < 1)
        {
            break;
        }
        printf("Rechenschritte iterativ: %d\n", collatzIterative(collatzNumber));
        printf("Rechenschritte rekusiv:  %d\n", collatzRekursive(collatzNumber));
    }
    return 0;
}

int collatzIterative(int number)
{
    int counter = 0;
    while (number != 1)
    {
        if (number % 2 == 0)
        {
            number = number / 2;
        }
        else
        {
            number = 3 * number + 1;
        }
        counter++;
    }
    return counter;
}

int collatzRekursive(int number)
{
    if (number == 1)
    {
        return 0;
    }
    if (number % 2 == 0)
    {
        return 1 + collatzRekursive(number / 2);
    }
    else
    {
        return 1 + collatzRekursive(3 * number + 1);
    }
}