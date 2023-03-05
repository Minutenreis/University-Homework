#include <stdio.h>
int add(int a, int b);
int mult(int a, int b);

int main()
{
    int a;
    int b;
    printf("Geben Sie a >= 0 und b >= 0 als a b ein: ");
    scanf("%d %d", &a, &b);
    if (a < 0 || b < 0)
    {
        printf("Ungueltige Eingabe\n");
        return 0;
    }
    printf("%d + %d = %d\n", a, b, add(a, b));
    printf("%d * %d = %d\n", a, b, mult(a, b));
    return 0;
}

int add(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    return add(a + 1, b - 1);
}

int mult(int a, int b)
{
    if (b == 0)
    {
        return 0;
    }
    return add(a, mult(a, b - 1));
}