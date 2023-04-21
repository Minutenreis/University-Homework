#include <stdio.h>
int *populateArray(int array[], int arrayLength);
int linearSearch(int seachedNumber, int array[], int arrayLength, int *lenLin);
int binarySearch(int searchedNumber, int array[], int start, int end, int *lenBin);

int main()
{
    int test[100];
    populateArray(test, 100);
    int searchedNumber;
    int lenBin = 0, lenLin = 0;
    printf("Geben sie eine Zahl ein, die Sie suchen; Array enthaelt alle ganzen Zahlen von 0 - 99 an selbigem Index\n");
    scanf("%d", &searchedNumber);
    printf("Die Zahl befindet sich an Index %d, linaer ermittelt\n", linearSearch(searchedNumber, test, 100, &lenLin));
    printf("Die Zahl befindet sich an Index %d, binear ermittelt\n", binarySearch(searchedNumber, test, 0, 99, &lenBin));
    printf("binaere Laufzeit: %d\n", lenBin);
    printf("lineare Laufzeit: %d\n", lenLin);
    return 0;
}

int *populateArray(int array[], int arrayLength)
{
    for (int i = 0; i <= arrayLength - 1; i++)
    {
        array[i] = i;
    }
    return array;
}

int linearSearch(int seachedNumber, int array[], int arrayLength, int *lenLin)
{
    for (int i = 0; i <= arrayLength - 1; i++)
    {
        (*lenLin)++;
        if (seachedNumber == array[i])
        {
            return i;
        }
    }
    return -1;
}

int binarySearch(int searchedNumber, int array[], int start, int end, int *lenBin)
{
    (*lenBin)++;
    int center = (start + end) / 2; //"obere Mitte"
    if (end < start)
    {
        return -1;
    }
    else if (searchedNumber == array[center])
    {
        return center;
    }
    else if (searchedNumber > array[center])
    {
        return binarySearch(searchedNumber, array, center + 1, end, lenBin);
    }
    else
    {
        return binarySearch(searchedNumber, array, start, center - 1, lenBin);
    }
}
