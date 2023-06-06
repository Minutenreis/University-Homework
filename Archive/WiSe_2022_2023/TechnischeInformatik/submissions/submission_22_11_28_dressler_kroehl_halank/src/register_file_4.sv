module register_file_4( input  logic       i_clk,
                        input  logic [1:0] i_reg_read_0,
                        input  logic [1:0] i_reg_read_1,
                        input  logic [1:0] i_reg_write,
                        input  logic [3:0] i_port_write,
                        input  logic       i_write_enable,
                        output logic [3:0] o_port_read_0,
                        output logic [3:0] o_port_read_1 );
    
    logic [3:0] l_one_hot;
    logic l_and_0, l_and_1, l_and_2, l_and_3;
    logic [3:0] l_reg_0, l_reg_1, l_reg_2, l_reg_3;

    decoder_2_4 m_decoder_2_4_0(.i_binary(i_reg_write), .o_one_hot(l_one_hot));

    and and_0(l_and_0, l_one_hot[0], i_write_enable);
    and and_1(l_and_1, l_one_hot[1], i_write_enable);
    and and_2(l_and_2, l_one_hot[2], i_write_enable);
    and and_3(l_and_3, l_one_hot[3], i_write_enable);

    register_en_4 m_register_en_4_0(.i_clk(i_clk), .i_d(i_port_write), .i_en(l_and_0), .o_q(l_reg_0));
    register_en_4 m_register_en_4_1(.i_clk(i_clk), .i_d(i_port_write), .i_en(l_and_1), .o_q(l_reg_1));
    register_en_4 m_register_en_4_2(.i_clk(i_clk), .i_d(i_port_write), .i_en(l_and_2), .o_q(l_reg_2));
    register_en_4 m_register_en_4_3(.i_clk(i_clk), .i_d(i_port_write), .i_en(l_and_3), .o_q(l_reg_3));

    mux_4 #(.N(4)) m_mux_4_0(.i_in0(l_reg_0), .i_in1(l_reg_1), .i_in2(l_reg_2), .i_in3(l_reg_3), .i_s(i_reg_read_0), .o_out(o_port_read_0));
    mux_4 #(.N(4)) m_mux_4_1(.i_in0(l_reg_0), .i_in1(l_reg_1), .i_in2(l_reg_2), .i_in3(l_reg_3), .i_s(i_reg_read_1), .o_out(o_port_read_1));

endmodule