#include <stdint.h>

// returns n-th fibonacci number
uint64_t fibonacci_c( uint64_t i_n ) {
  if( i_n <= 1 ) return i_n;

  uint64_t l_tmp_0 = 0;
  uint64_t l_tmp_1 = 1;
  uint64_t l_tmp_2 = 0;

  for( uint64_t l_va = 1; l_va < i_n; l_va++ ) {
    l_tmp_2 = l_tmp_0 + l_tmp_1;
    l_tmp_0 = l_tmp_1;
    l_tmp_1 = l_tmp_2;
  }

  return l_tmp_2;
}