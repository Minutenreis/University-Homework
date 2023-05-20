.text
.type showcase_fmla_element, %function
.global showcase_fmla_element

showcase_fmla_element:
    str d8, [sp, #-16]!
    
    ld1 {v0.4s}, [x0]
    ld1 {v4.4s}, [x1]
    ld1 {v8.4s}, [x2]

    fmla v8.4s, v0.4s, v4.s[2]

    st1 {v8.4s}, [x2]

    ldr d8, [sp], #16

    ret
