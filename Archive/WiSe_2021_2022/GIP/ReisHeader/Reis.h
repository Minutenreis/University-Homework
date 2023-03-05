int intPow(int base, int exponent)
{
    int power = 1;
    for(int i = 1; i <=exponent; i++)
    {
        power *= base;
    }
    return power;
}