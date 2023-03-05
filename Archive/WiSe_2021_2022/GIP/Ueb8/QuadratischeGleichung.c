#include <stdio.h>
#include <math.h>

int solveQuadratic(double, double, double, double *, double *);
int solveLinear(double, double, double *);
int solve(double, double, double, double *, double *);

int main(void)
{
    double a, b, c;
    printf("Geben Sie ihre Gleichung ax^2+bx+c=0\nals a b c an:");
    scanf("%lf %lf %lf", &a, &b, &c);
    double x1, x2;
    int anzahl = solve(a, b, c, &x1, &x2);
    if (!anzahl)
        printf("keine Loesung");
    else if (anzahl == 1)
        printf("eine Loesung x: %lf", x1);
    else if (anzahl > 1)
        printf("zwei Loesungen x1: %lf x2: %lf", x1, x2);
    return 0;
}

int solve(double a, double b, double c, double *x1, double *x2)
{
    if (a != 0)
    {
        return solveQuadratic(a, b, c, x1, x2);
    }
    else if (b != 0)
    {
        return solveLinear(b, c, x1);
    }
    else
    {
        return 0; // da laut der Aufgabe keine Loesung unendlich vorgesehen ist (0x^2+0x+0=0), kann hier keine Loesung rauskommen.
    }
}

int solveQuadratic(double a, double b, double c, double *x1, double *x2)
{
    double diskriminante = b * b - 4 * a * c;
    if (diskriminante < 0)
    {
        return 0; // komplexe Ergebnisse
    }
    else if (diskriminante == 0)
    {
        *x1 = -b / (2 * a);
        return 1; // Scheitelpunkt auf der x-Achse
    }
    else
    {
        *x1 = (-b + sqrt(diskriminante)) / (2 * a);
        *x2 = (-b - sqrt(diskriminante)) / (2 * a);
        return 2; //"Normalfall"
    }
}

int solveLinear(double b, double c, double *x1)
{
    *x1 = -c / b;
    return 1; // Schnittpunkt Gerade Achse
}
