/**
D Latch consisting of 2 SR-Latches
@param i_clk clock input
@param i_d Data input
@param o_q Q output
@param o_qn Q inverted output
*/
module d_latch(
    input logic i_clk, 
    input logic i_d, 
    output logic o_q, 
    output logic o_qn);

    logic l_dn, l_r, l_s;
    not m_not_0(l_dn, i_d);

    and m_and_0(l_r, i_clk, l_dn);
    and m_and_1(l_s, i_clk, i_d);

    sr_latch m_sr_latch_0(.i_s(l_s), .i_r(l_r), .o_q(o_q), .o_qn(o_qn));

endmodule