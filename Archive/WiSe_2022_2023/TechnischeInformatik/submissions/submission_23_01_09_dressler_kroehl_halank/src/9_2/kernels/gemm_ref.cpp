void gemm_ref_mnk( float const  * i_a,
                   float const  * i_b,
                   float        * io_c,
                   unsigned int   i_m,
                   unsigned int   i_n,
                   unsigned int   i_k,
                   unsigned int   i_lda,
                   unsigned int   i_ldb,
                   unsigned int   i_ldc ) {
  for( unsigned int l_m = 0; l_m < i_m; l_m++ ) {
    for( unsigned int l_n = 0; l_n < i_n; l_n++ ) {
      for( unsigned int l_k = 0; l_k < i_k; l_k++ ) {
        io_c[ l_n*i_ldc + l_m ] += i_a[ l_k*i_lda + l_m ] * i_b[ l_n*i_ldb + l_k ];
      }
    }
  }
}
