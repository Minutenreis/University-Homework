/**
 * Reference implementation of a GEMM (C+=AB).
 *
 * @param i_a pointer to A (column-major).
 * @param i_b pointer to B (column-major)
 * @param io_c pointer to C (column-major).
 * @param i_m BLAS parameter M.
 * @param i_n BLAS parameter N.
 * @param i_k BLAS parameter K.
 * @param i_lda leading dimension of A.
 * @param i_ldb leading dimension of B.
 * @param i_ldc leading dimension of C.
 **/
void gemm_ref_mnk( float const  * i_a,
                   float const  * i_b,
                   float        * io_c,
                   unsigned int   i_m,
                   unsigned int   i_n,
                   unsigned int   i_k,
                   unsigned int   i_lda,
                   unsigned int   i_ldb,
                   unsigned int   i_ldc );