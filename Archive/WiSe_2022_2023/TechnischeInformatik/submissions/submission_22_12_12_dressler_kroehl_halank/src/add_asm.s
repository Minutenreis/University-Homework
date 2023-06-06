.text
.type add_asm, %function
.global add_asm
    //adds two arrays and outputs the result to a third array
add_asm:    //void add_asm(int i_n_values, int* i_a, int* i_b, int* o_c)
    mov x4, #0   //l_va = 0, iteration counter
    mov x5, #0   //j = 0, offset; l_va * 8

loop:
    cmp x4, x0   //l_va < i_n_values
    b.ge end_loop
    ldr x10, [x1, x5]   //l_tmp_a = i_a[i]
    ldr x11, [x2, x5]   //l_tmp_b = i_b[i]
    add x12, x10, x11   //l_tmp_c = l_tmp_a + l_tmp_b
    str x12, [x3, x5]   //o_c[i] = l_tmp_c
    add x4, x4, #1   //l_va++
    add x5, x5, #8   //j += 8
    b loop

end_loop:
    ret
    
    .size   add_asm, (. - add_asm)
