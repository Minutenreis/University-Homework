#include <stdio.h>

int power(int a, int exponent)
{
    int base = a;
    if (exponent == 0)
    {
        return 1;
    }
    else
    {
        for (int i = 1; i < exponent; i++)
        {
            a *= base;
        }
    }
    return a;
}

int main()
{
    int base, exponent, result;
    printf("Eingabe: ");
    scanf("%d %d", &base, &exponent);
    result = power(base, exponent);
    printf("%d", result);
    return 0;
}