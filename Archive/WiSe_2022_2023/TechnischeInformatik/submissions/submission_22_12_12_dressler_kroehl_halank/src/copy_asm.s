        .text
        .align 4
        .type   copy_asm, %function
        .global copy_asm
        // copies first 7 values from source array to destination array
copy_asm:       //void copy_asm(int *src, int *dest)     
        ldr x10, [x0]
        ldr x11, [x0, #8]
        ldr x12, [x0, #16]
        ldr x13, [x0, #24]
        ldr x14, [x0, #32]
        ldr x15, [x0, #40]
        ldr x16, [x0, #48]

        str x10, [x1]
        str x11, [x1, #8]
        str x12, [x1, #16]
        str x13, [x1, #24]
        str x14, [x1, #32]
        str x15, [x1, #40]
        str x16, [x1, #48]

        ret
        .size   copy_asm, (. - copy_asm)

        .text
        .align 4
        .type   copy_asm_loop, %function
        .global copy_asm_loop
        // copies first 7 values from source array to destination array with a loop
copy_asm_loop:  //void copy_asm_loop(int *src, int *dest)
        mov x2 , #0 // i = 0, iteration counter
        mov x3 , #0 // j = 0, offset
        
loop:
        cmp x2, #7 // if i >= 7, return
        b.ge end_loop
        ldr x10, [x0, x3] // temp = src[i]
        str x10, [x1, x3] // dest[i] = temp
        add x3, x3, #8 // j += 8
        add x2, x2, #1 // i += 1
        b loop

end_loop:
        ret
        
