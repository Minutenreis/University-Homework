#include <stdio.h>
#include <stdlib.h>

int getMedian(int C[], int n) // O(1)
{
    if (n % 2 == 0)
        return C[n / 2 - 1];
    else
        return C[n / 2];
}

int cmpfunc(const void *a, const void *b) // O(1)
{
    return (*(int *)a - *(int *)b);
}

int median(int A[], int B[], int n) // O(log n)
{
    if (n == 0) // Leeres Array => kein Element
    {
        return 0; // O(1)
    }
    else if (n == 1) // Ein Element in jedem Array => Durchschnitt der Beiden
    {
        return A[0]<B[0]? A[0]:B[0]; // O(1)
    }
    else if (n == 2) // Zwei Elemente in jedem Array, Median = Median der 4 Elemente
    {
        int C[] = {A[0], A[1], B[0], B[1]}; // O(1)
        qsort(C, 4, sizeof(int), cmpfunc);  // O(4 log 4) = O(1)
        return getMedian(C, 4);             // O(1)
    }

    int mA = getMedian(A, n); // O(1)
    int mB = getMedian(B, n); // O(1)

    if (mA == mB) // mA <= m <= mB => m = mA = mB
    {
        return mA; // O(1)
    }
    else if (mA < mB) // mA < m < mB => suchen auf der oberen Hälfte von A und unteren von B
    {
        return median(A + n / 2, B, n - n / 2); // log n Aufrufe
    }
    else // mA > m > mB => suchen auf der oberen Hälfte von B und unteren von A
    {
        return median(A, B + n / 2, n - n / 2); // log n Aufrufe
    }
}

int main(int argc, char const *argv[])
{
    int A[] = {1, 5, 6, 7, 8};
    int B[] = {2, 3, 4, 9, 10};
    printf("%d\n", median(A, B, 5));
    return 0;
}
