#include <stdio.h>
#include <stdlib.h>

void magicSquareTester(int **quadrat, int seitenlaenge);
int **initialize2DArray(int seitenlaenge);

int main()
{
    int **square = initialize2DArray(3);
    square[0][0] = 1;
    square[1][0] = 1;
    square[2][0] = 1;
    square[0][1] = 1;
    square[1][1] = 1;
    square[2][1] = 1;
    square[0][2] = 1;
    square[1][2] = 1;
    square[2][2] = 1;

    magicSquareTester(square, 3);
    return 0;
}

int **initialize2DArray(int seitenlaenge)
{
    int **quadrat = calloc(seitenlaenge, sizeof(int *));
    for (int i = 0; i < seitenlaenge; i++)
    {
        quadrat[i] = (int *)calloc(seitenlaenge, sizeof(int));
    }
    return quadrat;
}

void magicSquareTester(int **quadrat, int seitenlaenge)
{
    int referenz = 0;
    int liniensumme;
    int valueCheck;
    for (int spalte = 0; spalte < seitenlaenge; spalte++) // referenzwert
    {
        referenz += quadrat[spalte][0];
    }
    for (int zeile = 1; zeile < seitenlaenge; zeile++)
    {
        liniensumme = 0;
        for (int spalte = 0; spalte < seitenlaenge; spalte++)
        {
            liniensumme += quadrat[spalte][zeile];
        }
        if (liniensumme != referenz)
        {
            printf("zeilensumme (%d) in Zeile %d stimmt nicht mit der Summe der obersten Zeile (%d) ueberein", liniensumme, zeile, referenz);
            return;
        }
    }
    for (int spalte = 0; spalte < seitenlaenge; spalte++)
    {
        liniensumme = 0;
        for (int zeile = 0; zeile < seitenlaenge; zeile++)
        {
            liniensumme += quadrat[spalte][zeile];
        }
        if (liniensumme != referenz)
        {
            printf("Spaltensumme (%d) in Spalte %d stimmt nicht mit der Summe der obersten Zeile (%d) ueberein", liniensumme, spalte, referenz);
            return;
        }
    }
    liniensumme = 0;
    for (int diagonale = 0; diagonale < seitenlaenge; diagonale++)
    {
        liniensumme += quadrat[diagonale][diagonale];
    }
    if (liniensumme != referenz)
    {
        printf("Diagonalensumme (%d) der Diagonale links oben => rechts unten stimmt nicht mit der Summe der obersten Zeile (%d) ueberein", liniensumme, referenz);
        return;
    }
    liniensumme = 0;
    for (int diagonale = 0; diagonale < seitenlaenge; diagonale++)
    {
        liniensumme += quadrat[diagonale][seitenlaenge - 1 - diagonale];
    }
    if (liniensumme != referenz)
    {
        printf("Diagonalensumme (%d) der Diagonale links unten => rechts oben stimmt nicht mit der Summe der obersten Zeile (%d) ueberein", liniensumme, referenz);
        return;
    }
    for (int zeile = 0; zeile < seitenlaenge; zeile++)
    {
        for (int spalte = 0; spalte < seitenlaenge; spalte++)
        {
            valueCheck = quadrat[spalte][zeile];
            liniensumme = 0;
            for (int zeile = 0; zeile < seitenlaenge; zeile++)
            {
                for (int spalte = 0; spalte < seitenlaenge; spalte++)
                {
                    if(quadrat[spalte][zeile] == valueCheck)
                    {
                        liniensumme++;
                    }
                }
            }
            if (liniensumme != 1)
            {
                printf("Die Zahl %d ist %d mal aufgetreten", valueCheck, liniensumme);
                return;
            }
        }
    }
    printf("Success");
    return;
}