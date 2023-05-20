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
        // store callee-saved registers
        stp x19, x20, [sp, #-16]!              //wir nutzen nur x0-x2, müssen x19-x30 actually gestored werden?
        stp x21, x22, [sp, #-16]!
        stp x23, x24, [sp, #-16]!
        stp x25, x26, [sp, #-16]!
        stp x27, x28, [sp, #-16]!
        stp x29, x30, [sp, #-16]!

        stp  d8,  d9, [sp, #-16]!               //same with d8-d15
        stp d10, d11, [sp, #-16]!
        stp d12, d13, [sp, #-16]!
        stp d14, d15, [sp, #-16]!


        // load A
        ld1 {v0.4s, v1.4s, v2.4s, v3.4s},   [x0]

        // load B
        ld1 {v4.4s, v5.4s, v6.4s, v7.4s},   [x1]

        // load C
        ld1 {v8.4s, v9.4s, v10.4s, v11.4s}, [x2]

        // TODO: perform the fmas

        fmla v8.4S, v0.4S, v4.S[0]
        fmla v9.4S, v0.4S, v5.S[0]
        fmla v10.4S, v0.4S, v6.S[0]
        fmla v11.4S, v0.4S, v7.S[0]

        fmla v8.4S, v1.4S, v4.S[1]
        fmla v9.4S, v1.4S, v5.S[1]
        fmla v10.4S, v1.4S, v6.S[1]
        fmla v11.4S, v1.4S, v7.S[1]

        fmla v8.4S, v2.4S, v4.S[2]
        fmla v9.4S, v2.4S, v5.S[2]
        fmla v10.4S, v2.4S, v6.S[2]
        fmla v11.4S, v2.4S, v7.S[2]

        fmla v8.4S, v3.4S, v4.S[3]
        fmla v9.4S, v3.4S, v5.S[3]
        fmla v10.4S, v3.4S, v6.S[3]
        fmla v11.4S, v3.4S, v7.S[3]
        
        // store C
        st1 {v8.4s, v9.4s, v10.4s, v11.4s}, [x2]

        // restore callee-saved registers
        ldp d14, d15, [sp], #16
        ldp d12, d13, [sp], #16
        ldp d10, d11, [sp], #16
        ldp  d8,  d9, [sp], #16

        ldp x29, x30, [sp], #16
        ldp x27, x28, [sp], #16
        ldp x25, x26, [sp], #16
        ldp x23, x24, [sp], #16
        ldp x21, x22, [sp], #16
        ldp x19, x20, [sp], #16

        ret
        .size gemm_asm_asimd_4_4_4, (. - gemm_asm_asimd_4_4_4)

