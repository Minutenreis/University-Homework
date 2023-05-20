/**
4 bit register
@Param i_clk clock
@Param i_en enable
@Param i_d data
@Param o_q output
*/
module register_en_4( input  logic       i_clk,
                      input  logic       i_en,
                      input  logic [3:0] i_d,
                      output logic [3:0] o_q );
    d_flip_flop_en m_dffen_0 ( .i_clk(i_clk), .i_en(i_en), .i_d(i_d[0]), .o_q(o_q[0]) );
    d_flip_flop_en m_dffen_1 ( .i_clk(i_clk), .i_en(i_en), .i_d(i_d[1]), .o_q(o_q[1]) );
    d_flip_flop_en m_dffen_2 ( .i_clk(i_clk), .i_en(i_en), .i_d(i_d[2]), .o_q(o_q[2]) );
    d_flip_flop_en m_dffen_3 ( .i_clk(i_clk), .i_en(i_en), .i_d(i_d[3]), .o_q(o_q[3]) );

endmodule