/**
 * 2er Mux Testbench
 **/
module mux_2_tb;
    logic l_s;
    logic [63:0] l_in0, l_in1, l_out;

    mux_2 #(.N(64)) m_dut(.i_s(l_s), .i_in0(l_in0), .i_in1(l_in1), .o_out(l_out));

    initial begin
        $dumpfile("mux_2_tb.vcd");
        $dumpvars;
        l_s = 0;
        l_in0 = 0;
        l_in1 = 1;
        #10;
        assert(l_out === 0);

        l_s = 1;
        l_in0 = 0;
        l_in1 = 1;
        #10;
        assert(l_out === 1);

        l_s = 0;
        l_in0 = 2**63-1;
        l_in1 = 2**62-1;
        #10;
        assert(l_out === 2**63-1);

        l_s = 1;
        l_in0 = 2**63-1;
        l_in1 = 2**62-1;
        #10;
        assert(l_out === 2**62-1);

        $finish;
    end
endmodule