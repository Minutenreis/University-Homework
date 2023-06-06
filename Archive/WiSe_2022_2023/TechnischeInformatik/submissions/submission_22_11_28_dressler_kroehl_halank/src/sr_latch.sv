/**
SR Latch
@param i_r reset input
@param i_s set input
@param o_q state output
@param o_nq inverted state output
**/
module sr_latch(
    input logic i_r, 
    input logic i_s, 
    output logic o_q, 
    output logic o_qn);

    nor m_nor_0(o_q, i_r, o_qn);
    nor m_nor_1(o_qn, i_s, o_q);

endmodule