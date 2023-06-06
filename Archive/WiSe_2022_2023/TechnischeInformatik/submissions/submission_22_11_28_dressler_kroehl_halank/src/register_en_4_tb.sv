/**
 *Testbench for register_en_4
 **/
module register_en_4_tb;
    logic l_clk, l_en;
    logic [3:0] l_d, l_q;
    register_en_4 m_dut(.i_clk(l_clk), .i_d(l_d), .i_en(l_en), .o_q(l_q));

    always begin // clock with period #10
        l_clk <= 1'b1;
        #5;
        l_clk <= 1'b0;
        #5;
    end

    initial begin
        $dumpfile("register_en_4_tb.vcd");
        $dumpvars;
        l_d = 4'b1111;
        l_en = 1'b1;
        #11;
        assert(l_q == 4'b1111);

        l_en=1'b0;
        #1;
        l_d = 4'b0000;
        #9;
        assert(l_q == 4'b1111);

        l_en=1'b1;
        #10;
        assert(l_q == 4'b0000);
        $finish;
    end
endmodule