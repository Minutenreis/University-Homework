#include <cstdint>
#include <cstdlib>
#include <iostream>

extern "C" {
  void add_c( uint64_t         i_n_values,
              uint64_t const * i_a,
              uint64_t const * i_b,
              uint64_t       * o_c );
  void add_asm( uint64_t         i_n_values,
                uint64_t const * i_a,
                uint64_t const * i_b,
                uint64_t       * o_c );
}

int main() {
  uint64_t l_n_values = 10;

  // init pointers
  uint64_t * l_a = nullptr;
  uint64_t * l_b = nullptr;
  uint64_t * l_c_0 = nullptr;
  uint64_t * l_c_1 = nullptr;

  // allocate memory
  l_a   = (uint64_t *) new uint64_t[ l_n_values ];
  l_b   = (uint64_t *) new uint64_t[ l_n_values ];
  l_c_0 = (uint64_t *) new uint64_t[ l_n_values ];
  l_c_1 = (uint64_t *) new uint64_t[ l_n_values ];

  // init arrays
  for( std::size_t l_va = 0; l_va < l_n_values; l_va++ ) {
    l_a[l_va] = l_va;
    l_b[l_va] = l_va*2;
    l_c_0[l_va] = 0;
    l_c_1[l_va] = 0;
  }

  // add_c
  std::cout << "### calling add_c ###" << std::endl;
  add_c( l_n_values,
         l_a,
         l_b,
         l_c_0 );

  for( std::size_t l_va = 0; l_va < l_n_values; l_va++ ) {
    std::cout << l_a[l_va] << " / " << l_b[l_va] << " / " << l_c_0[l_va] << std::endl;
  }

  // add_asm
  std::cout << "### calling add_asm ###" << std::endl;
  add_asm( l_n_values,
           l_a,
           l_b,
           l_c_1 );

  for( std::size_t l_va = 0; l_va < l_n_values; l_va++ ) {
    std::cout << l_a[l_va] << " / " << l_b[l_va] << " / " << l_c_1[l_va] << std::endl;
  }

  // free memory
  delete [] l_a;
  delete [] l_b;
  delete [] l_c_0;
  delete [] l_c_1;

  return EXIT_SUCCESS;
}