        .text
        .type gemm_asm_asimd_4_4_4, %function
        .global gemm_asm_asimd_4_4_4
        /*
         * Performs the matrix-matrix multiplication C+=A*B
         * with the shapes (4x4) = (4x4) * (4x4).
         * The input data is of type float.
         * Uses vector instructions.
         *
         * @param x0 pointer to A.
         * @param x1 pointer to B.
         * @param x2 pointer to C.
         */ 
gemm_asm_asimd_4_4_4:

        // load A
        ld1 {v0.4s, v1.4s, v2.4s, v3.4s},   [x0]

        // load B
        ld1 {v4.4s, v5.4s, v6.4s, v7.4s},   [x1]

        // load C
        ld1 {v16.4s, v17.4s, v18.4s, v19.4s}, [x2]

        // TODO: perform the fmas

        fmla v16.4S, v0.4S, v4.S[0]
        fmla v17.4S, v0.4S, v5.S[0]
        fmla v18.4S, v0.4S, v6.S[0]
        fmla v19.4S, v0.4S, v7.S[0]

        fmla v16.4S, v1.4S, v4.S[1]
        fmla v17.4S, v1.4S, v5.S[1]
        fmla v18.4S, v1.4S, v6.S[1]
        fmla v19.4S, v1.4S, v7.S[1]

        fmla v16.4S, v2.4S, v4.S[2]
        fmla v17.4S, v2.4S, v5.S[2]
        fmla v18.4S, v2.4S, v6.S[2]
        fmla v19.4S, v2.4S, v7.S[2]

        fmla v16.4S, v3.4S, v4.S[3]
        fmla v17.4S, v3.4S, v5.S[3]
        fmla v18.4S, v3.4S, v6.S[3]
        fmla v19.4S, v3.4S, v7.S[3]
        
        // store C
        st1 {v16.4s, v17.4s, v18.4s, v19.4s}, [x2]

        ret
        .size gemm_asm_asimd_4_4_4, (. - gemm_asm_asimd_4_4_4)

