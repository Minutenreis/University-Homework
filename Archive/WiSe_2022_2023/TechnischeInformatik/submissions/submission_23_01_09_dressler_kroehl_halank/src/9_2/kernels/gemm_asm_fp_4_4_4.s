        .text
        .type gemm_asm_fp_4_4_4, %function
        .global gemm_asm_fp_4_4_4
        /*
         * Performs the matrix-matrix multiplication C+=A*B
         * with the shapes (4x4) = (4x4) * (4x4).
         * The input data is of type float.
         * Uses scalar instructions.
         *
         * @param x0 pointer to A.
         * @param x1 pointer to B.
         * @param x2 pointer to C.
         */ 
gemm_asm_fp_4_4_4:
        // store
        stp x19, x20, [sp, #-16]!
        stp x21, x22, [sp, #-16]!
        stp x23, x24, [sp, #-16]!
        stp x25, x26, [sp, #-16]!
        stp x27, x28, [sp, #-16]!
        stp x29, x30, [sp, #-16]!

        stp  d8,  d9, [sp, #-16]!
        stp d10, d11, [sp, #-16]!
        stp d12, d13, [sp, #-16]!
        stp d14, d15, [sp, #-16]!

        // load C
        ldp  s0,  s1, [x2], #8
        ldp  s2,  s3, [x2], #8
        ldp  s4,  s5, [x2], #8
        ldp  s6,  s7, [x2], #8
        ldp  s8,  s9, [x2], #8
        ldp s10, s11, [x2], #8
        ldp s12, s13, [x2], #8
        ldp s14, s15, [x2]
        sub x2, x2, #7*8

        // load first column of A
        ldp s16, s17, [x0], #8
        ldp s18, s19, [x0], #8

        // load first row of B
        ldr s20, [x1], #4*4
        ldr s21, [x1], #4*4
        ldr s22, [x1], #4*4
        ldr s23, [x1], #-3*4*4 + 4

        // perform fmas
        fmadd  s0, s16, s20,  s0 
        fmadd  s1, s17, s20,  s1
        fmadd  s2, s18, s20,  s2
        fmadd  s3, s19, s20,  s3

        fmadd  s4, s16, s21,  s4
        fmadd  s5, s17, s21,  s5
        fmadd  s6, s18, s21,  s6
        fmadd  s7, s19, s21,  s7

        fmadd  s8, s16, s22,  s8
        fmadd  s9, s17, s22,  s9
        fmadd s10, s18, s22, s10
        fmadd s11, s19, s22, s11

        fmadd s12, s16, s23, s12
        fmadd s13, s17, s23, s13
        fmadd s14, s18, s23, s14
        fmadd s15, s19, s23, s15


        // load second column of A
        ldp s16, s17, [x0], #8
        ldp s18, s19, [x0], #8

        // load second row of B
        ldr s20, [x1], #4*4
        ldr s21, [x1], #4*4
        ldr s22, [x1], #4*4
        ldr s23, [x1], #-3*4*4 + 4

        // perform fmas
        fmadd  s0, s16, s20,  s0 
        fmadd  s1, s17, s20,  s1
        fmadd  s2, s18, s20,  s2
        fmadd  s3, s19, s20,  s3

        fmadd  s4, s16, s21,  s4
        fmadd  s5, s17, s21,  s5
        fmadd  s6, s18, s21,  s6
        fmadd  s7, s19, s21,  s7

        fmadd  s8, s16, s22,  s8
        fmadd  s9, s17, s22,  s9
        fmadd s10, s18, s22, s10
        fmadd s11, s19, s22, s11

        fmadd s12, s16, s23, s12
        fmadd s13, s17, s23, s13
        fmadd s14, s18, s23, s14
        fmadd s15, s19, s23, s15


        // load third column of A
        ldp s16, s17, [x0], #8
        ldp s18, s19, [x0], #8

        // load third row of B
        ldr s20, [x1], #4*4
        ldr s21, [x1], #4*4
        ldr s22, [x1], #4*4
        ldr s23, [x1], #-3*4*4 + 4

        // perform fmas
        fmadd  s0, s16, s20,  s0 
        fmadd  s1, s17, s20,  s1
        fmadd  s2, s18, s20,  s2
        fmadd  s3, s19, s20,  s3

        fmadd  s4, s16, s21,  s4
        fmadd  s5, s17, s21,  s5
        fmadd  s6, s18, s21,  s6
        fmadd  s7, s19, s21,  s7

        fmadd  s8, s16, s22,  s8
        fmadd  s9, s17, s22,  s9
        fmadd s10, s18, s22, s10
        fmadd s11, s19, s22, s11

        fmadd s12, s16, s23, s12
        fmadd s13, s17, s23, s13
        fmadd s14, s18, s23, s14
        fmadd s15, s19, s23, s15


        // load fourth column of A
        ldp s16, s17, [x0], #8
        ldp s18, s19, [x0], #8

        // load fourth row of B
        ldr s20, [x1], #4*4
        ldr s21, [x1], #4*4
        ldr s22, [x1], #4*4
        ldr s23, [x1], #-3*4*4 + 4

        // perform fmas
        fmadd  s0, s16, s20,  s0 
        fmadd  s1, s17, s20,  s1
        fmadd  s2, s18, s20,  s2
        fmadd  s3, s19, s20,  s3

        fmadd  s4, s16, s21,  s4
        fmadd  s5, s17, s21,  s5
        fmadd  s6, s18, s21,  s6
        fmadd  s7, s19, s21,  s7

        fmadd  s8, s16, s22,  s8
        fmadd  s9, s17, s22,  s9
        fmadd s10, s18, s22, s10
        fmadd s11, s19, s22, s11

        fmadd s12, s16, s23, s12
        fmadd s13, s17, s23, s13
        fmadd s14, s18, s23, s14
        fmadd s15, s19, s23, s15

        // store C
        stp  s0,  s1, [x2], #8
        stp  s2,  s3, [x2], #8
        stp  s4,  s5, [x2], #8
        stp  s6,  s7, [x2], #8
        stp  s8,  s9, [x2], #8
        stp s10, s11, [x2], #8
        stp s12, s13, [x2], #8
        stp s14, s15, [x2]

        // restore
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
        .size gemm_asm_fp_4_4_4, (. - gemm_asm_fp_4_4_4)

