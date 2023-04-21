#include <stdio.h>
#include <stdlib.h>
char *decipher(char string[], int key);
char *encipher(char string[], int key);

int main()
{
    char string[1000];
    char example[] = "YLHOH NDPHQ DOOPDHKOLFK CX GHU XHEHUCHXJXQJ HLQHQ JURVVHQ IHKOHU JHPDFKW CX KDEHQ DOV VLH YRQ GHQ EDHXPHQ KHUXQWHUJHNRPPHQ ZDUHQ XQG HLQLJH VDJWHQ VFKRQ GLH EDHXPH VHLHQ HLQ KROCZHJ JHZHVHQ GLH RCHDQH KDHWWH PDQ QLHPDOV YHUODVVHQ GXHUIHQ";
    int key;
    int decision;
    printf("Geben sie ihren zu verschluesselnden String ein\n");
    scanf("%[^\n]", string);
    printf("Geben sie einen Key zwischen 0 und 26 ein\n");
    scanf("%d", &key);
    if (key < 0 || key > 26)
    {
        printf("Ungueltige Eingabe\n");
        return 0;
    }
    printf("Wollen sie \n 1 verschluesseln \n 2 entschluesseln\n 3 Beispieltext entschluesseln\n");
    scanf("%d", &decision);
    if (decision == 1)
    {
        printf("%s\n", encipher(string, key));
    }
    else if (decision == 2)
    {
        printf("%s\n", decipher(string, key));
    }
    else
    {
        printf("%s\n", decipher(example, key));
    }
    return 0;
}

char *decipher(char string[], int key)
{
    int i = 0;
    while (string[i] != '\0')
    {
        if (string[i] >= 'A' && string[i] <= 'Z')
        {
            string[i] = (string[i] - 'A' - key + 26) % 26 + 'A'; //-A | +A => modulo nur aufs alphabet anwenden, 0 = A, 25 = Z
        }
        else if (string[i] >= 'a' && string[i] <= 'z')
        {
            string[i] = (string[i] - 'a' - key + 26) % 26 + 'a';
        }
        i++;
    }
    return string;
}

char *encipher(char string[], int key)
{
    return decipher(string, -key);
}