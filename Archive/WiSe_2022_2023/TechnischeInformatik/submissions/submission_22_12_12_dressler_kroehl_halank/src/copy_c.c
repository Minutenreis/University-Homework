#include <stdint.h>

void copy_c( uint64_t const * i_a,
             uint64_t       * i_b ) {
  uint64_t l_tmp_0 = i_a[0];
  uint64_t l_tmp_1 = i_a[1];
  uint64_t l_tmp_2 = i_a[2];
  uint64_t l_tmp_3 = i_a[3];
  uint64_t l_tmp_4 = i_a[4];
  uint64_t l_tmp_5 = i_a[5];
  uint64_t l_tmp_6 = i_a[6];

  i_b[0] = l_tmp_0;
  i_b[1] = l_tmp_1;
  i_b[2] = l_tmp_2;
  i_b[3] = l_tmp_3;
  i_b[4] = l_tmp_4;
  i_b[5] = l_tmp_5;
  i_b[6] = l_tmp_6;
}