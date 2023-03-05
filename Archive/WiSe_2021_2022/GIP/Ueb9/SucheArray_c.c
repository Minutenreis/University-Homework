#include <stdio.h>
int *populateArray(int Array[], int ArrayLength);
int linearSearch(int gesuchteZahl, int Suchbereich[], int ArrayLength);
int binarySearch(int gesuchteZahl, int *suchbereich, int start, int ende);

int main()
{
    int test[100];
    populateArray(test, 100);
    int searchedNumber;
    printf("Geben sie eine Zahl ein, die Sie suchen; Array enthaelt alle ganzen Zahlen von 0 - 99 an selbigem Index\n");
    scanf("%d", &searchedNumber);
    printf("Die Zahl befindet sich an Index %d, linaer ermittelt\n", linearSearch(searchedNumber, test, 100));
    printf("Die Zahl befindet sich an Index %d, binear ermittelt\n", binarySearch(searchedNumber, test, 0, 99));
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

int linearSearch(int searchedNumber, int array[], int arrayLength)
{
    for (int i = 0; i <= arrayLength - 1; i++)
    {
        if (searchedNumber == array[i])
        {
            return i;
        }
    }
    return -1;
}

int binarySearch(int searchedNumber, int *array, int start, int end)
{
    int center = (start + end) / 2;
    if (end < start)
    {
        return -1;
    }
    else if (searchedNumber == *(array + center))
    {
        return center;
    }
    else if (searchedNumber > *(array + center))
    {
        return binarySearch(searchedNumber, array, center + 1, end);
    }
    else
    {
        return binarySearch(searchedNumber, array, start, center - 1);
    }
}