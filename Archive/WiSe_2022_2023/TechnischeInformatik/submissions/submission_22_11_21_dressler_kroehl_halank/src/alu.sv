/**
 * Basic ALU
 **/
module alu #(parameter N=64) ( input  logic [N-1:0] i_a,
                                                 i_b,
                            input  logic [1:0]   i_alu_ctrl,
                            output logic [N-1:0] o_result,
                            output logic         o_carry_out );
    logic [N-1:0] l_mux, l_adder, l_and, l_or, l_notb;

    assign l_notb = ~i_b;
    assign l_and  = i_a & i_b;
    assign l_or   = i_a | i_b;
    mux_2 #(.N(N)) mux_2_0(.i_s(i_alu_ctrl[0:0]), .i_in0(i_b), .i_in1(l_notb), .o_out(l_mux));
    adder #(.N(N)) adder_0(.i_a(i_a), .i_b(l_mux),.i_carry_in(i_alu_ctrl[0:0]), .o_s(l_adder), .o_carry_out(o_carry_out));
    mux_4 #(.N(N)) mux_4_0(.i_s(i_alu_ctrl), .i_in0(l_adder), .i_in1(l_adder), .i_in2(l_and), .i_in3(l_or), .o_out(o_result));
endmodule