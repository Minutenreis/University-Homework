#include <stdint.h>

void add_c(uint64_t i_n_values,
           uint64_t const *i_a,
           uint64_t const *i_b,
           uint64_t *o_c)
{
  for (uint64_t l_va = 0; l_va < i_n_values; l_va++)
  {
    uint64_t l_tmp_a = i_a[l_va];
    uint64_t l_tmp_b = i_b[l_va];
    uint64_t l_tmp_c = l_tmp_a + l_tmp_b;

    o_c[l_va] = l_tmp_c;
  }
}
