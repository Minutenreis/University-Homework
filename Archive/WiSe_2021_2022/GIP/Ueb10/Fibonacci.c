#include <stdio.h>
int fibonacci(int n);

int main()
{
    int number;
    printf("Geben sie an, welche Fibonacci Zahl sie bestimmt haben wollen.\n");
    scanf("%d", &number);
    if(number>=0)
    {
        printf("f(%d)=%d\n", number, fibonacci(number));
    }
    else
    {
        printf("Ungueltige Eingabe\n");
    }
    return 0;
}

int fibonacci(int n)
{
    if(n <= 1)
    {
        return 1;
    }
    return fibonacci(n-1)+fibonacci(n-2);
}