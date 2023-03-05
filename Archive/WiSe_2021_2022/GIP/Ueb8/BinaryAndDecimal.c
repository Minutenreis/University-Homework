#include <stdio.h>
void decimal(void);
void binary(void);
int decimalValid(int);
int binaryValid(unsigned long long int);
int binaryToDecimal(unsigned long long int);
unsigned long long int decimalToBinary(int);

int main(void)
{
    int binOrDec;
    printf("Wollen Sie ... \n");
    printf("1 eine Dezimalzahl in eine Binaerzahl umwandeln?\n");
    printf("2 eine Binaerzahl in eine Dezimalzahl umwandeln?\n");
    scanf("%d", &binOrDec);
    switch (binOrDec)
    {
    case 1:
        decimal();
        break;
    case 2:
        binary();
        break;
    default:
        decimal();
    }
    return 0;
}

void decimal(void)
{
    int decimal;
    unsigned long long int binary;
    printf("Geben Sie eine Dezimalzahl ein: "); // max 2^20-1 (sonst Stackoverflow bei Binary)
    scanf("%d", &decimal);
    if (decimalValid(decimal))
    {
        binary = decimalToBinary(decimal);
        printf("Dezimalzahl: %d\t\t Binaerzahl: %llu", decimal, binary);
    }
    else
    {
        printf("Ungueltige Eingabe");
    }
}

void binary(void)
{
    int decimal;
    unsigned long long int binary;
    printf("Geben Sie eine Binaerzahl ein: "); // max 2^20-1 (sonst Stackoverflow)
    scanf("%llu", &binary);
    if (binaryValid(binary))
    {
        decimal = binaryToDecimal(binary);
        printf("Binaerzahl: %llu\t\t Dezimalzahl: %d", binary, decimal);
    }
    else
    {
        printf("Ungueltige Eingabe");
    }
}

int binaryToDecimal(unsigned long long int binary)
{
    int decimal = 0;
    int faktor = 1;
    while (binary > 0)
    {
        decimal += (binary % 10) * faktor;
        binary /= 10;
        faktor *= 2;
    }
    return decimal;
}

unsigned long long int decimalToBinary(int decimal)
{
    unsigned long long int binary = 0;
    int faktor = 1;
    while (decimal > 0)
    {
        binary += (decimal % 2) * faktor;
        decimal /= 2;
        faktor *= 10;
    }
    return binary;
}

int binaryValid(unsigned long long int binary)
{
    if (binary < 0)
    {
        return 0;
    }

    while (binary > 0)
    {
        if (binary % 10 != 1 && binary % 10 != 0)
        {
            return 0;
        }
        binary /= 10;
    }
    return 1;
}

int decimalValid(int decimal)
{
    if (decimal < 0 || decimal >= 1048576)
    {
        return 0;
    }
    return 1;
}