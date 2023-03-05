#include <stdio.h>
#include <math.h>

int main()
{   
    double sideLength(float x1, float y1, float x2, float y2);
    double x1, y1, x2, y2, x3, y3, s, a, b, c, A;
    printf("\nKoordinaten P1 x1 y1: ");
    scanf("%lf %lf", &x1, &y1);
    printf("\nKoordinaten P2 x2 y2: ");
    scanf("%lf %lf", &x2, &y2);
    printf("\nKoordinaten P3 x3 y3: ");
    scanf("%lf %lf", &x3, &y3);
    a = sideLength(x1, y1, x2, y2);
    b = sideLength(x1, y1, x3, y3);
    c = sideLength(x3, y3, x2, y2);
    s = (a + b + c) / 2;
    A = sqrt(s*(s-a)*(s-b)*(s-c));
    if(A == 0)
    {
        printf("Flaecheninhalt: 0 (kein Dreieck / entartetes Dreieck)");
    }
    else 
    {
        printf("Flaecheninhalt: %lf", A);
    }
}

double sideLength(float x1, float y1, float x2, float y2)
{
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}