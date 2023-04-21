#include <stdio.h>
#include <stdlib.h>

int **initialize2DArray(int sidelength);
int **magicSquare(int sidelength);
void printSquare(int **square, int sidelength);
void freeSquare(int **square, int sidelength);

int main()
{
    int sidelength;
    printf("Geben Sie eine ungerade Seitenlaenge fuer ihr gewuenschtes magisches Quadrat an.\n");
    scanf("%d", &sidelength);
    if (sidelength < 1 || sidelength % 2 != 1)
    {
        printf("Ungueltige Eingabe.\n");
        return 1;
    }
    printSquare(magicSquare(sidelength), sidelength);
    return 0;
}

int **initialize2DArray(int sidelength)
{
    int **square = malloc(sidelength * sizeof(int *));
    for (int i = 0; i < sidelength; i++)
    {
        square[i] = calloc(sidelength, sizeof(int));
    }
    return square;
}

void printSquare(int **square, int sidelength)
{
    for (int zeile = 0; zeile < sidelength; zeile++)
    {
        for (int spalte = 0; spalte < sidelength; spalte++)
        {
            printf("%d\t", square[spalte][zeile]);
        }
        printf("\n");
    }
    freeSquare(square, sidelength);
}

void freeSquare(int **square, int sidelength)
{
    for (int i = 0; i < sidelength; i++)
    {
        free(square[i]);
    }
    free(square);
}

int **magicSquare(int sidelength)
{
    int **square = initialize2DArray(sidelength);
    int column = sidelength / 2;
    int row = (sidelength / 2 + 1) % sidelength;
    square[column][row] = 1;
    for(int i = 2; i <= sidelength * sidelength; i++)
    {
        column = (column + 1) % sidelength;
        row = (row + 1) % sidelength;
        if (square[column][row] == 0)
        {
            square[column][row] = i;
        }
        else
        {
            while (square[column][row] != 0)
            {
                column = (column + sidelength - 1) % sidelength; //+seitenlaenge um -1 % seitenlaenge = -1 zu entgehen
                row = (row + 1) % sidelength;
            }
            square[column][row] = i;
        }
    }
    return square;
}