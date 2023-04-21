#include <stdio.h>
int *populateArray(int array[], int arrayLength);
int linearSearch(int searchedNumber, int array[], int arrayLength);
int binarySearch(int searchedNumber, int array[], int start, int end);
int implementieren(int searchedNumber);

int main()
{
    int searchedNumber;
    printf("Geben sie eine Zahl ein, diese wird in einem Array aller Primzahlen bis 100 gesucht, bei Erfolg wird ihre position ausgegeben\n");
    scanf("%d", &searchedNumber);
    int primes[25] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
    int result = binarySearch(searchedNumber, primes, 0, 24) + 1; //+1 damit die x. Primzahl ausgegeben wird
    if (result != 0)
    {
        printf("Ihre gesuchte Zahl ist die %d. Primzahl.\n", result);
    }
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

int binarySearch(int searchedNumber, int array[], int start, int end)
{
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
        return binarySearch(searchedNumber, array, center + 1, end);
    }
    else
    {
        return binarySearch(searchedNumber, array, start, center - 1);
    }
}
