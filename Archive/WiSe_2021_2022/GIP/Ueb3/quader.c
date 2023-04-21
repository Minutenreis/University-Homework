#include <stdio.h>
#include <math.h>

int main()
{
    float x1, y1, z1, x2, y2, z2, dx, dy, dz, V, Ao, s;
    printf("Geben Sie die Koordinaten der Eckpunke als x1 y1 z1 x2 y2 z2 ein: ");
    scanf("%f%f%f%f%f%f", &x1, &y1, &z1, &x2, &y2, &z2);
    dx = fabs(x1 - x2);
    dy = fabs(y1 - y2);
    dz = fabs(z1 - z2);
    if ((dx == 0) || (dy == 0) || (dz == 0))
    {
        printf("Eine Kantenlaenge ist 0, die Koordinaten bilden keinen Quader.");
        return 0;
    }
    V = dx * dy * dz;
    Ao = 2 * dx * dy + 2 * dy * dz + 2 * dx * dz;
    s = 4 * dx + 4 * dy + 4 * dz;
    printf("Der Quader hat ein Volumen von %.2f, einen Oberflaecheninhalt von %.2f und eine Gesamtlaenge aller Kanten von %.2f ", V, Ao, s);
    return 0;
}