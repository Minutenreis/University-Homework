#include <stdint.h>

uint64_t machine_code_c() {
  uint64_t l_tmp_0 = 3;
  uint64_t l_tmp_1 = 0;
  uint64_t l_tmp_2 = 0;

  while( 1 ) {
    l_tmp_0--;
    l_tmp_1 = l_tmp_1 + 3;
    l_tmp_2 = l_tmp_2 + 7;

    if( l_tmp_0 == 0 ) break;
  }

  l_tmp_0 = l_tmp_1 + l_tmp_2;

  return l_tmp_0;
}