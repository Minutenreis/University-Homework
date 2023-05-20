.type low_lvl_0, %function
.global low_lvl_0
low_lvl_0:
    ret // return input in w0

    .size   low_lvl_0, (. - low_lvl_0)

.type low_lvl_1, %function
.global low_lvl_1
low_lvl_1:
    mov x0, #0  // return 0
    ret

    .size   low_lvl_1, (. - low_lvl_1)

.type low_lvl_2, %function
.global low_lvl_2
low_lvl_2:
    cmp w0, #32     // if (input < 32)
    b.lt low_lvl_2_1// return 1
    mov w0, #0      // else return 0
    ret
low_lvl_2_1:
    mov w0, #1
    ret


    .size   low_lvl_2, (. - low_lvl_2)

.type low_lvl_3, %function
.global low_lvl_3
low_lvl_3:
    ldr w3, [x0]    // w3 = input
    cmp w3, #25     // if (input < 25)
    b.lt if_3       // o_result = 1
    mov w2, #0      // else o_result = 0
    str w2, [x1]
    ret
if_3:
    mov w2, #1      // o_result = 1
    str w2, [x1]
    ret

    .size   low_lvl_3, (. - low_lvl_3)

.type low_lvl_4, %function
.global low_lvl_4
low_lvl_4:
    cmp w0, w1      // if (x >= y)
    b.ge else_4_y   // jump else
    cmp w0, w2      // or if (x >= z)
    b.ge else_4_y   // jump else
    mov w0, #1      // x<y && x<z return 1
    ret

else_4_y:
    cmp w1, w2      // if (y >= z)
    b.ge else_4     // return 3
    mov w0, #2      // y<z return 2
    ret

else_4:
    mov w0, #3      // return 3
    ret

    .size   low_lvl_4, (. - low_lvl_4)

.type low_lvl_5, %function
.global low_lvl_5
low_lvl_5:
    mov w2, #0   // i=0

    cmp w0, #0  // if (l_va == 0)
    b.le end_5  // return

    ldr w3, [x1]  // sum = io_value

loop_5:
    cmp w2, w0  // if (i < n)
    b.ge end_save_5  // break
    add w3, w3, #1   // sum += 1
    add w2, w2, #1   // i += 1
    b loop_5     // loop

end_save_5:
    str w3, [x1]    // io_value = sum

end_5:
    ret

    .size   low_lvl_5, (. - low_lvl_5)

.type low_lvl_6, %function
.global low_lvl_6
low_lvl_6:
    //x0 = l_va
    ldr x3, [x2] // x3 = io_value

loop_6:
    add x3, x3, x1 // x3 += i_inc
    subs x0, x0, #1 // l_va -= 1
    b.ne loop_6 // if (l_va != 0) loop

    str x3, [x2] // io_value = x3
    ret

    .size   low_lvl_6, (. - low_lvl_6)

.type low_lvl_7, %function
.global low_lvl_7
low_lvl_7:
    mov x3, #0  // i = 0
loop_7:
    cmp x3, x0  // if (i < n)
    b.ge end_7  // break
    ldr x4, [x1, x3, lsl #3]    // x4 = i_valuesIn[i]
    str x4, [x2, x3, lsl #3]    // i_valuesOut[i] = x4

    add x3, x3, #1  // i += 1
    b loop_7    // loop


end_7:
    ret

    .size   low_lvl_7, (. - low_lvl_7)
    