/**
 *Testbench for d_flip_flop_en
 **/
module d_flip_flop_en_tb;
    logic l_clk, l_d, l_en, l_q, l_qn;

    d_flip_flop_en m_dut(.i_clk(l_clk), .i_d(l_d), .i_en(l_en), .o_q(l_q), .o_qn(l_qn));

    always begin // clock with period #10
        l_clk <= 1'b1;
        #5;
        l_clk <= 1'b0;
        #5;
    end

    initial begin
        $dumpfile("d_flip_flop_en_tb.vcd");
        $dumpvars;
    
        l_d = 1'b0;
        l_en = 1'b1;
        #11;
        assert(l_q === 1'b0);
        assert(l_qn === 1'b1);

        l_d = 1'b1;
        l_en = 1'b1;
        #10;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        l_en = 1'b0;
        #1;
        l_d = 1'b0;
        #9;
        assert(l_q === 1'b1);
        assert(l_qn === 1'b0);

        l_en = 1'b1;
        #10;
        assert(l_q === 1'b0);
        assert(l_qn === 1'b1);
        
        $finish;
    end
endmodule