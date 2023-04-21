#include <stdio.h>
#include <math.h>

int A1(int n);
int A2(int n);

int main(){
    int n = 2;
    while(n <= 64){
        printf("%d     A1: %d, A2: %d\n", n, A1(n), A2(n));
        n *= 2;
    }
    return 0;
}

int A1(int n){
    return n;
}

int A2(int n){
    return 2*n*n;
}