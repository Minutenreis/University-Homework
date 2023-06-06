/**
 *Testbench for d_latch
 **/
module d_latch_tb;
    logic l_clk, l_d, l_q, l_qn;

    d_latch m_dut(.i_clk(l_clk), .i_d(l_d), .o_q(l_q), .o_qn(l_qn));

    always begin // clock with period #10
        l_clk <= 1'b1;
        #5;
        l_clk <= 1'b0;
        #5;
    end

    initial begin
        $dumpfile("d_latch_tb.vcd");
        $dumpvars;
        l_d = 1'b0;
        #10;
        assert(l_q === 1'b0);
        assert(l_qn === 1'b1);

        l_d = 1'b1;
        #10;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        #6; //clock low
        l_d = 1'b0;
        #2;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        #12; //full clock cycle
        assert(l_q === 1'b0);
        assert(l_qn === 1'b1);

        $finish;
    end
endmodule