/**
 *Testbench for sr_latch
 **/
module sr_latch_tb;
    logic l_r, l_s, l_q, l_qn;

    sr_latch m_dut(.i_r(l_r), .i_s(l_s), .o_q(l_q), .o_qn(l_qn));

    initial begin
        $dumpfile("sr_latch_tb.vcd");
        $dumpvars;

        l_r = 1'b0;
        l_s = 1'b1;
        #10;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        l_r = 1'b0;
        l_s = 1'b0;
        #10;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        l_r = 1'b1;
        l_s = 1'b0;
        #10;
        assert(l_q === 1'b0);
        assert(l_qn === 1'b1);
        $finish;
    end
endmodule