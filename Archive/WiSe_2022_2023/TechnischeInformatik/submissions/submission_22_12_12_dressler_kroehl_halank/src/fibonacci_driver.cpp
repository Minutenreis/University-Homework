#include <cstdint>

#include <cstdlib>

#include <iostream>


extern "C" {

  uint64_t fibonacci_c( uint64_t i_id );

  uint64_t fibonacci_asm( uint64_t i_id );

}


int main() {

  uint64_t l_id = 50;

  uint64_t l_number_0 = 0;

  uint64_t l_number_1 = 0;


  // fibonacci_c

  std::cout << "### fibonacci_c ###" << std::endl;

  l_number_0 = fibonacci_c( l_id );


  std::cout << "id / number: " << l_id << " / " << l_number_0 << std::endl;


  // fibonacci_asm

  std::cout << "### fibonacci_asm ###" << std::endl;

  l_number_1 = fibonacci_asm( l_id );


  std::cout << "id / number: " << l_id << " / " << l_number_1 << std::endl;


  return EXIT_SUCCESS;

}