#include <stdio.h>

int main()
{
    int i = 5;
    int j = 7;
    int *p = &i;
    int *q = &j;
    void print();
    printf("Anweisung\ti\tj\tp\t\t*p\tq\t\t*q\n");
    print("Start\t", i, j, p, q);
    i = *p * *q;
    print("i = *p * *q;", i, j, p, q);

    *p = 12;
    print("*p = 12;", i, j, p, q);

    q = p;
    print("q = p;\t", i, j, p, q);

    j = i / 2;
    print("j = i / 2;", i, j, p, q);

    (*q)++;
    print("(*q)++;\t", i, j, p, q);

    j = *q;
    print("j = *q;\t", i, j, p, q);
}

void print(char s[], int i, int j, int *p, int *q)
{
    printf("%s\t%d\t%d\t%p\t%d\t%p\t%d\n", s, i, j, p, *p, q, *q);
}
