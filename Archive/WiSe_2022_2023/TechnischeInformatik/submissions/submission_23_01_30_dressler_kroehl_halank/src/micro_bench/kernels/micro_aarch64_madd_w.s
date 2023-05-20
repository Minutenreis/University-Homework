        .align 4
        .text
        .type micro_aarch64_madd_w_independent, %function
        .global micro_aarch64_madd_w_independent
        /*
         * Microbenchmark benchmarking the throughput of independet MADD instructions.
         *
         * @param x0: number of times the benchmarking code is executed.
         * @return x0: number of instructions per loop iteration.
         */ 
micro_aarch64_madd_w_independent:
        // PCS: store required data in GPRs on stack
        stp x19, x20, [sp, #-16]!
        stp x21, x22, [sp, #-16]!
        stp x23, x24, [sp, #-16]!
        stp x25, x26, [sp, #-16]!
        stp x27, x28, [sp, #-16]!
        stp x29, x30, [sp, #-16]!

        // reset GPRs
        eor w1, w1, w1
        eor w2, w2, w2
        eor w3, w3, w3
        eor w4, w4, w4
        eor w5, w5, w5
        eor w6, w6, w6
        eor w7, w7, w7
        eor w8, w8, w8
        eor w9, w9, w9
        eor w10, w10, w10
        eor w11, w11, w11
        eor w12, w12, w12
        eor w13, w13, w13
        eor w14, w14, w14
        eor w15, w15, w15
        eor w16, w16, w16
        eor w17, w17, w17
        eor w18, w18, w18
        eor w19, w19, w19
        eor w20, w20, w20
        eor w21, w21, w21
        eor w22, w22, w22
        eor w23, w23, w23
        eor w24, w24, w24
        eor w25, w25, w25
        eor w26, w26, w26
        eor w27, w27, w27
        eor w28, w28, w28
        eor w29, w29, w29
        eor w30, w30, w30

        // perform the operations
loop_repeat_w_independent:
        subs x0, x0, #1

        madd w2, w1, w1, w1
        madd w3, w1, w1, w1
        madd w4, w1, w1, w1
        madd w5, w1, w1, w1
        madd w6, w1, w1, w1
        madd w7, w1, w1, w1
        madd w8, w1, w1, w1
        madd w9, w1, w1, w1
        madd w10, w1, w1, w1
        madd w11, w1, w1, w1
        madd w12, w1, w1, w1
        madd w13, w1, w1, w1
        madd w14, w1, w1, w1
        madd w15, w1, w1, w1
        madd w16, w1, w1, w1

        b.ne loop_repeat_w_independent

        // PCS: restore GPRs
        ldp x29, x30, [sp], #16
        ldp x27, x28, [sp], #16
        ldp x25, x26, [sp], #16
        ldp x23, x24, [sp], #16
        ldp x21, x22, [sp], #16
        ldp x19, x20, [sp], #16

        mov x0, #15

        ret
        .size micro_aarch64_madd_w_raw_rn, (. - micro_aarch64_madd_w_raw_rn)

        .align 4
        .text
        .type micro_aarch64_madd_w_raw_rn, %function
        .global micro_aarch64_madd_w_raw_rn
        /*
         * Microbenchmark benchmarking the throughput of independet MADD instructions.
         *
         * @param x0: number of times the benchmarking code is executed.
         * @return x0: number of instructions per loop iteration.
         */ 
micro_aarch64_madd_w_raw_rn:
        // PCS: store required data in GPRs on stack
        stp x19, x20, [sp, #-16]!
        stp x21, x22, [sp, #-16]!
        stp x23, x24, [sp, #-16]!
        stp x25, x26, [sp, #-16]!
        stp x27, x28, [sp, #-16]!
        stp x29, x30, [sp, #-16]!

        // reset GPRs
        eor w1, w1, w1
        eor w2, w2, w2
        eor w3, w3, w3
        eor w4, w4, w4
        eor w5, w5, w5
        eor w6, w6, w6
        eor w7, w7, w7
        eor w8, w8, w8
        eor w9, w9, w9
        eor w10, w10, w10
        eor w11, w11, w11
        eor w12, w12, w12
        eor w13, w13, w13
        eor w14, w14, w14
        eor w15, w15, w15
        eor w16, w16, w16
        eor w17, w17, w17
        eor w18, w18, w18
        eor w19, w19, w19
        eor w20, w20, w20
        eor w21, w21, w21
        eor w22, w22, w22
        eor w23, w23, w23
        eor w24, w24, w24
        eor w25, w25, w25
        eor w26, w26, w26
        eor w27, w27, w27
        eor w28, w28, w28
        eor w29, w29, w29
        eor w30, w30, w30

        // perform the operations
loop_repeat_w_raw_rn:
        subs x0, x0, #1

        madd w2, w16, w1, w1
        madd w3, w2, w1, w1
        madd w4, w3, w1, w1
        madd w5, w4, w1, w1
        madd w6, w5, w1, w1
        madd w7, w6, w1, w1
        madd w8, w7, w1, w1
        madd w9, w8, w1, w1
        madd w10, w9, w1, w1
        madd w11, w10, w1, w1
        madd w12, w11, w1, w1
        madd w13, w12, w1, w1
        madd w14, w13, w1, w1
        madd w15, w14, w1, w1
        madd w16, w15, w1, w1


        b.ne loop_repeat_w_raw_rn

        // PCS: restore GPRs
        ldp x29, x30, [sp], #16
        ldp x27, x28, [sp], #16
        ldp x25, x26, [sp], #16
        ldp x23, x24, [sp], #16
        ldp x21, x22, [sp], #16
        ldp x19, x20, [sp], #16

        mov x0, #15

        ret
        .size micro_aarch64_madd_w_raw_rn, (. - micro_aarch64_madd_w_raw_rn)