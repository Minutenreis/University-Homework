#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    int ** dreieck = calloc(n, sizeof(int *)); // oder int ** dreieck = calloc(n, sizeof(int *));
    for (int i = 0; i < n; i++)
    {
        dreieck[i] = (int *)calloc(i + 1, sizeof(int));
        for (int j = 0; j <= i; j++)
        {
            if ((j == 0) || (j == i))
                dreieck[i][j] = 1;
            else
                dreieck[i][j] = dreieck[i - 1][j - 1] + dreieck[i - 1][j];
            printf("%2d ", dreieck[i][j]);
        }
        printf("\n");
    }
    return 0;
}
