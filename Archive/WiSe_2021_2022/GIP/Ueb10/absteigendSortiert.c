#include <stdio.h>
int absteigend(long long n);

int main()
{
    long long number;
    printf("Geben Sie ihre Zahl zum testen ein\n");
    scanf("%lld", &number);
    if (number < 0)
    {
        printf("Ungueltige Eingabe\n");
        return 0;
    }
    if (absteigend(number))
    {
        printf("%lld ist absteigend sortiert\n", number);
    }
    else
    {
        printf("%lld ist NICHT absteigend sortiert\n", number);
    }
    return 0;
}

int absteigend(long long n)
{
    if (n <= 9)
    {
        return 1;
    }
    if (n % 10 < (n / 10) % 10)
    {
        return absteigend(n / 10);
    }
    return 0;
}