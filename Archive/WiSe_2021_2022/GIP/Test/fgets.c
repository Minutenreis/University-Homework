#include <stdio.h>
#include <stdlib.h>

int main()
{
    char string[1024];
    fgets(string, 1024, stdin);
    for (int i = 0; i < 1024; i++)
    {
        printf("%c", string[i]);
    }
    return 0;
}