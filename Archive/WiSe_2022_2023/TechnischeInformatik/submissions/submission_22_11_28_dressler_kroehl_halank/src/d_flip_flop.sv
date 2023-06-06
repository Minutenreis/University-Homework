/**
Rising Edge D Flipflop consisting of 2 D Latches
@param clk clock input
@param d data input
@param q output
@param qn inverted output
*/
module d_flip_flop(
    input logic i_clk,
    input logic i_d,
    output logic o_q,
    output logic o_qn
);
    logic l_clkn, l_x;

    not m_not_0(l_clkn, i_clk);

    d_latch m_d_latch_0(.i_clk(l_clkn), .i_d(i_d), .o_q(l_x));
    d_latch m_d_latch_1(.i_clk(i_clk), .i_d(l_x), .o_q(o_q), .o_qn(o_qn));

endmodule