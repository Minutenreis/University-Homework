#include <stdio.h>

int main() {
    float Answer1, Answer2, Answer3;
    int Answer4;
    char Answer5;
    printf("Was ist 4.5 + 2.2?\n ");
    scanf("%f", &Answer1);
    printf("Was ist 1/3 auf 2 Nachkommastellen genau?\n ");
    scanf("%f", &Answer2);
    printf("Was ist 3 * 1.3?\n ");
    scanf("%f", &Answer3);
    printf("Was ist 1 + 1?\n ");
    scanf("%d", &Answer4);
    printf("Aus was besteht Diamand? \n a) Kohlenstoff \t b) Kohlenstoffdioxid \n c) Uran \t d) Silicium \n ");
    scanf(" %c", &Answer5);
    printf("%c, %d, %f, %f, %f", Answer5, Answer4, Answer3, Answer2, Answer1);
    return 0;
}