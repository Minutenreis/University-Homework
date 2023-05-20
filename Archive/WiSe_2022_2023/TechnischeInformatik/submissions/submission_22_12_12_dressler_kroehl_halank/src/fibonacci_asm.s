        .text
        .align 4
        .type   fibonacci_asm, %function
        .global fibonacci_asm
        // returns the nth fibonacci number
fibonacci_asm:       //uint64_t fibonacci_asm(uint64_t i_n)
    cmp x0, #1        //if (i_n <= 1) return i_n;
    b.eq return

    mov x3, #1        //l_va = 1;
    mov x4, #0        //l_tmp_0 = 0;
    mov x5, #1        //l_tmp_1 = 1;
    mov x6, #0        //l_tmp_2 = 0;
loop:
    cmp x3, x0        //while(l_va < i_n);
    b.ge end_loop
    add x6, x5, x4  //l_tmp_2 = l_tmp_1 + l_tmp_0;
    mov x4, x5      //l_tmp_0 = l_tmp_1;
    mov x5, x6      //l_tmp_1 = l_tmp_2;
    add x3, x3, #1  //l_va += 1
    b loop

end_loop:
    mov x0, x6      //return l_tmp_2;
    b return

return:
    ret

    .size   fibonacci_asm, (. - fibonacci_asm)
