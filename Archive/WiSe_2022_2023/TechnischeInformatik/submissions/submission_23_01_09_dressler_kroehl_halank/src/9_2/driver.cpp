#include <iostream>
#include <cmath>
#include <chrono>
#include "kernels/gemm_ref.h"

const unsigned int l_n_repetitions = 100000000;

extern "C" {
  void gemm_asm_fp_4_4_4( float const * i_a,
                          float const * i_b,
                          float       * io_c );
  void gemm_asm_asimd_4_4_4( float const * i_a,
                             float const * i_b,
                             float       * io_c );
}

/**
 * Computes the maximum absolute element-wise difference of matrices.
 *
 * @param i_mat0 first matrix (column-major).
 * @param i_mat1 second matrix (column-major).
 * @param i_m number of rows.
 * @param i_n number of columns.
 * @param i_ld leading dimension.
 **/
float max_diff( float const * i_mat0,
                float const * i_mat1,
                unsigned int  i_m,
                unsigned int  i_n,
                unsigned int  i_ld ) {
  float l_max_diff = 0;

  for( unsigned int l_m = 0; l_m < i_m; l_m++ ) {
    for( unsigned int l_n = 0; l_n < i_n; l_n++ ) {
      float l_diff = i_mat0[ l_n*i_ld + l_m ] - i_mat1[ l_n*i_ld + l_m ];
      l_diff = std::abs( l_diff );

      l_max_diff = std::max( l_max_diff, l_diff );
    }
  }

  return l_max_diff;
}

int main() {
  // allocate memory
  std::size_t l_size = 64*64;
  float * l_a = new float[ l_size ];
  float * l_b = new float[ l_size ];
  float * l_c = new float[ l_size ];
  float * l_c_ref = new float[ l_size ];

  // init seed
  srand48( time(NULL) );

  std::chrono::steady_clock::time_point l_tp0, l_tp1;
  std::chrono::duration<double> l_dur;
  float l_max_diff = 0;
  double l_g_flops =0;

  /*
   * FP 4, 4, 4
   */
  std::cout << "testing gemm_asm_fp_4_4_4 kernel" << std::endl;

  // reset data
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_a[l_id] = (float) drand48();
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_b[l_id] = (float) drand48();
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_c[l_id] = drand48();
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_c_ref[l_id] = l_c[l_id];
  }

  // run reference implementation
  gemm_ref_mnk( l_a,
                l_b,
                l_c_ref,
                4,
                4,
                4,
                4,
                4,
                4 );

  // run assembly kernel
  gemm_asm_fp_4_4_4( l_a,
                     l_b,
                     l_c );

  l_max_diff = max_diff( l_c_ref,
                         l_c,
                         4,
                         4,
                         4 );

  std::cout << "  maximum difference: " << l_max_diff << "\n";

  // time scalar kernel
  l_tp0 = std::chrono::steady_clock::now();
  for( unsigned int l_re = 0; l_re < l_n_repetitions; l_re++ ) {
    gemm_asm_fp_4_4_4( l_a,
                       l_b,
                       l_c );
  }
  l_tp1 = std::chrono::steady_clock::now();

  l_dur = std::chrono::duration_cast< std::chrono::duration< double> >( l_tp1 - l_tp0 );

  std::cout << "  duration: " << l_dur.count() << " seconds" << std::endl;
  l_g_flops  = l_n_repetitions;
  l_g_flops *= 4 * 4 * 4 * 2;
  l_g_flops *= 1.0E-9;
  l_g_flops /= l_dur.count();
  std::cout << "  GFLOPS: " << l_g_flops << std::endl;


  /*
   * ASIMD 4, 4, 4
   */
  std::cout << "testing gemm_asm_asimd_4_4_4 kernel" << std::endl;

  // reset data
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_a[l_id] = (float) drand48();
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_b[l_id] = (float) drand48();
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_c[l_id] = drand48();;
  }
  for( unsigned int l_id = 0; l_id < l_size; l_id++ ) {
    l_c_ref[l_id] = l_c[l_id];
  }

  // run reference implementation
  gemm_ref_mnk( l_a,
                l_b,
                l_c_ref,
                4,
                4,
                4,
                4,
                4,
                4 );

  // run assembly kernel
  gemm_asm_asimd_4_4_4( l_a,
                        l_b,
                        l_c );

  l_max_diff = max_diff( l_c_ref,
                         l_c,
                         4,
                         4,
                         4 );

  std::cout << "  maximum difference: " << l_max_diff << "\n";

  // time asimd kernel
  l_tp0 = std::chrono::steady_clock::now();
  for( unsigned int l_re = 0; l_re < l_n_repetitions; l_re++ ) {
    gemm_asm_asimd_4_4_4( l_a,
                          l_b,
                          l_c );
  }
  l_tp1 = std::chrono::steady_clock::now();

  l_dur = std::chrono::duration_cast< std::chrono::duration< double> >( l_tp1 - l_tp0 );

  std::cout << "  duration: " << l_dur.count() << " seconds" << std::endl;
  l_g_flops  = l_n_repetitions;
  l_g_flops *= 4 * 4 * 4 * 2;
  l_g_flops *= 1.0E-9;
  l_g_flops /= l_dur.count();
  std::cout << "  GFLOPS: " << l_g_flops << std::endl;

  // free memory
  delete[] l_a;
  delete[] l_b;
  delete[] l_c;
  delete[] l_c_ref;

  return EXIT_SUCCESS;
}
