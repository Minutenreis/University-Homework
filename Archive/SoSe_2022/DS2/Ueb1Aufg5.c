#include <stdio.h>
unsigned long long smallestNumberFulfilling(int n);
unsigned long long intPow(int base, int exponent);
int numberOnes(unsigned long long n);
int numberZeroes(unsigned long long n);

int main(){
    int n;
    printf("Input: ");
    scanf("%d", &n);
    unsigned long long result = smallestNumberFulfilling(n);
    printf("\nresult: %llu\n", result);
    printf("%d x 1; %d x 0, Vielfaches: %llu\n", numberOnes(result), numberZeroes(result), result/n);
    return 0;
}

int numberOnes(unsigned long long n){
    int count = 0;
    while(n > 0){
        if(n % 10 == 1){
            count++;
        }
        n /= 10;
    }
    return count;
}

int numberZeroes(unsigned long long n){
    int count = 0;
    if(n == 0)
    {
        return 1;
    }
    while(n > 0){
        if(n % 10 == 0){
            count++;
        }
        n /= 10;
    }
    return count;
}

unsigned long long smallestNumberFulfilling(int n){
    unsigned long long result = 1;
    int length = 1;
    int onePosition = 0;
    if(n ==0){
        return 0;
    }
    while(result%n != 0){
        if (onePosition > 0)
        {
            result += intPow(10, onePosition-1);
            onePosition--;
        }
        else
        {
            result = intPow(10, length);
            length++;
            onePosition = length-1;
        }
    }
    return result;
}

unsigned long long intPow(int base, int exponent)
{
    unsigned long long power = 1;
    for(int i = 1; i <=exponent; i++)
    {
        power *= base;
    }
    return power;
}