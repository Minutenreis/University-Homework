module alu_nzcv #(parameter N=64) ( input  logic [N-1:0] i_a,
                                                      i_b,
                                 input  logic [1:0]   i_alu_ctrl,
                                 output logic [N-1:0] o_result,
                                 output logic [3:0]   o_nzcv );
    logic l_carry_out, l_not_alu_ctrl, l_xor,l_xor_3, l_nxor_3, l_and_overflow;
    logic [N-1:0] l_mux, l_adder, l_and, l_or, l_notb;


    assign l_notb = ~i_b;
    assign l_and  = i_a & i_b;
    assign l_or   = i_a | i_b;
    mux_2 #(.N(N)) mux_2_0(.i_s(i_alu_ctrl[0:0]), .i_in0(i_b), .i_in1(l_notb), .o_out(l_mux));
    adder #(.N(N)) adder_0(.i_a(i_a), .i_b(l_mux),.i_carry_in(i_alu_ctrl[0:0]), .o_s(l_adder), .o_carry_out(l_carry_out));
    mux_4 #(.N(N)) mux_4_0(.i_s(i_alu_ctrl), .i_in0(l_adder), .i_in1(l_adder), .i_in2(l_and), .i_in3(l_or), .o_out(o_result));

    //negative Flag
    assign o_nzcv[3] = o_result[N-1:N-1];

    //zero Flag
    assign o_nzcv[2] = (o_result[N-1:0] == 0);

    //carry flag
    not not_0(l_not_alu_ctrl, i_alu_ctrl[1:1]);
    and and_0(o_nzcv[1], l_not_alu_ctrl, l_carry_out);

    //overflow flag
    xor xor_0(l_xor, i_a[N-1:N-1], l_adder[N-1:N-1]);
    xor_3 xor_3_0(.o_res(l_xor_3), .i_in0(i_a[N-1:N-1]), .i_in1(i_b[N-1:N-1]), .i_in2(i_alu_ctrl[0:0]));
    not not_3_0(l_nxor_3, l_xor_3);
    and and_1(l_and_overflow, l_xor, l_nxor_3);
    and and_2(o_nzcv[0], l_not_alu_ctrl, l_and_overflow);

endmodule