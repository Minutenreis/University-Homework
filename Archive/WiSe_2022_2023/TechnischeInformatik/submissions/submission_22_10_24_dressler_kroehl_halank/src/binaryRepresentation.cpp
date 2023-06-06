#include <iostream>
#include <bitset>

int main()
{
    unsigned char l_data1 = 1;
    unsigned char l_data2 = 255;
    unsigned char l_data3 = l_data2 + 1;
    unsigned char l_data4 = 0xA1;
    unsigned char l_data5 = 0b1001011;
    unsigned char l_data6 = 'H';
    char l_data7 = -4;
    unsigned int l_data8 = 1u << 11;
    unsigned int l_data9 = l_data8 << 21;
    unsigned int l_data10 = 0xFFFFFFFF >> 5;
    unsigned int l_data11 = 0b1001 ^ 0b01111;
    unsigned int l_data12 = ~0b1001;
    unsigned int l_data13 = 0xF0 & 0b1010101;
    unsigned int l_data14 = 0b001 | 0b101;
    unsigned int l_data15 = 7743;
    int l_data16 = -7743;
    std::cout << "l_data1 = " << std::bitset< 8 >( l_data1 ) << std::endl;
    std::cout << "l_data2 = " << std::bitset< 8 >( l_data2 ) << std::endl;
    std::cout << "l_data3 = " << std::bitset< 8 >( l_data3 ) << std::endl;
    std::cout << "l_data4 = " << std::bitset< 8 >( l_data4 ) << std::endl;
    std::cout << "l_data5 = " << std::bitset< 8 >( l_data5 ) << std::endl;
    std::cout << "l_data6 = " << std::bitset< 8 >( l_data6 ) << std::endl;
    std::cout << "l_data7 = " << std::bitset< 8 >( l_data7 ) << std::endl;
    std::cout << "l_data8 = " << std::bitset< 32 >( l_data8 ) << std::endl;
    std::cout << "l_data9 = " << std::bitset< 32 >( l_data9 ) << std::endl;
    std::cout << "l_data10 = " << std::bitset< 32 >( l_data10 ) << std::endl;
    std::cout << "l_data11 = " << std::bitset< 32 >( l_data11 ) << std::endl;
    std::cout << "l_data12 = " << std::bitset< 32 >( l_data12 ) << std::endl;
    std::cout << "l_data13 = " << std::bitset< 32 >( l_data13 ) << std::endl;
    std::cout << "l_data14 = " << std::bitset< 32 >( l_data14 ) << std::endl;
    std::cout << "l_data15 = " << std::bitset< 32 >( l_data15 ) << std::endl;
    std::cout << "l_data16 = " << std::bitset< 32 >( l_data16 ) << std::endl;
}

    