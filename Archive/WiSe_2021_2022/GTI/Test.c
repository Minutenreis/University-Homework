#include <stdio.h>

int main()
{
    int A, B;

    scanf("%d", A);
    if (A >= 17)
    {
        B = 12;
    }
    else
    {
        B = 5 + A;
    }
    printf("%d",B);
    return 0;
}