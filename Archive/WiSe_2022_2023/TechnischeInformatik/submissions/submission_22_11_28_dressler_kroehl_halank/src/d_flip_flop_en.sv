/**
rising edge d flip flop with enable signal
*/
module d_flip_flop_en(
    input logic i_clk,
    input logic i_d,
    input logic i_en,
    output logic o_q,
    output logic o_qn
);

    logic l_mux;
    mux_2 #(.N(1)) m_mux_2_0(.i_in0(o_q), .i_in1(i_d), .i_s(i_en), .o_out(l_mux));

    d_flip_flop d_flip_flop_0(.i_clk(i_clk), .i_d(l_mux), .o_q(o_q), .o_qn(o_qn));

endmodule