#include <stdio.h>
#include <math.h>
double f1(double, double);
double f2(double, double);

int main(void)
{
    double x, y, f2(double, double);
    printf("Geben sie x und y im Format x y ein: ");
    scanf("%lf %lf", &x, &y);
    printf("f1(%lf,%lf)=%lf\n", x, y, f1(x, y));
    printf("f2(%lf,%lf)=%lf\n", x, y, f2(x, y));
    return 0;
}

double f1(double x, double y)
{
    if (x - y == 0)
    {
        printf("f1(%lf,%lf) enthaelt eine Division durch 0.\n", x, y);
        return 0;
    }
    return (x + y) / (x - y);
}

double f2(double x, double y)
{
    return sqrt(x * x + y * y);
}
