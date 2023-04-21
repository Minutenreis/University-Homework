#include <stdio.h>
int add(int a, int b);
int sub(int a, int b);
int mult(int a, int b);

int main()
{
    int a;
    int b;
    printf("Geben Sie a >= 0 und b >= 0 als a b ein: ");
    scanf("%d %d", &a, &b);
    printf("%d + %d = %d\n", a, b, add(a, b));
    printf("%d + %d = %d\n", a, b, sub(a, b));
    printf("%d * %d = %d\n", a, b, mult(a, b));
    return 0;
}

int add(int a, int b)
{
    if (b > 0)
    {
        return add(a + 1, b - 1);
    }
    else if (b < 0)
    {
        return add(a - 1, b + 1);
    }
    return a;
}

int sub(int a, int b)
{
    return add(a, -b);
}

int mult(int a, int b)
{
    if (b > 0)
    {
        return add(a, mult(a, b - 1));
    }
    else if (b < 0)
    {
        return add(-a, mult(a, b + 1));
    }
    return 0;
}