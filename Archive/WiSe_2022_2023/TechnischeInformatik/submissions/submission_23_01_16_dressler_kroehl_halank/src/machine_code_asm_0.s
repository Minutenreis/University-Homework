        .text
        .align 4
        .type   machine_code_asm_0, %function
        .global machine_code_asm_0
machine_code_asm_0:
        orr x0, xzr, #3
        and x1, x1, xzr
        and x2, x2, xzr

my_loop:
        subs x0, x0, #1
        add x1, x1, #3
        add x2, x2, #7
        b.ne my_loop

        add x0, x1, x2

        ret
        .size   machine_code_asm_0, (. - machine_code_asm_0)


        .text
        .align 4
        .type   machine_code_asm_1, %function
        .global machine_code_asm_1
	
machine_code_asm_1:		// TODO: implement machine code version
        
	.inst 0xb24007e0        //orr	x0, xzr, #0x3
	.inst 0x8a1f0021        //and	x1, x1, xzr
	.inst 0x8a1f0042        //and   x2, x2, xzr
	.inst 0xf1000400        //subs	x0, x0, #0x1
	.inst 0x91000c21        //add	x1, x1, #0x3
	.inst 0x91001c42        //add	x2, x2, #0x7
	.inst 0x54ffffa1        //b.ne	c <my_loop>  // b.any
	.inst 0x8b020020        //add	x0, x1, x2
	.inst 0xd65f03c0        //ret
        
        .size   machine_code_asm_1, (. - machine_code_asm_1)
        
