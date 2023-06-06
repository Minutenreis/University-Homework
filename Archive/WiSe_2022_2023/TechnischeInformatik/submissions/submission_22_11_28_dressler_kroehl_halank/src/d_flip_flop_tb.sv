/**
 *Testbench for d_flip_flop
 **/
module d_flip_flop_tb;
    logic l_clk, l_d, l_q, l_qn;

    d_flip_flop m_dut(.i_clk(l_clk), .i_d(l_d), .o_q(l_q), .o_qn(l_qn));

    always begin // clock with period #10
        l_clk <= 1'b1;
        #5;
        l_clk <= 1'b0;
        #5;
    end

    initial begin
        $dumpfile("d_flip_flop_tb.vcd");
        $dumpvars;

        l_d = 1'b0;
        #11;
        assert(l_q === 1'b0);

        l_d = 1'b1;
        #10;
        assert(l_q === 1'b1);

        l_d = 1'b0;
        #8;
        assert(l_q === 1'b1);

        #2;
        assert(l_q === 1'b0);

        $finish;
    end
endmodule