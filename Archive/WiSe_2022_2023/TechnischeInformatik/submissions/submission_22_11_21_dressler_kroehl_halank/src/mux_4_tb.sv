/**
 *Testbench for 4er Mux
 **/
module mux_4_tb;
    logic [1:0] l_s;
    logic [63:0] l_in0, l_in1, l_in2, l_in3, l_out;

    mux_4 #(.N(64)) m_dut(.i_s(l_s), .i_in0(l_in0), .i_in1(l_in1), .i_in2(l_in2), .i_in3(l_in3), .o_out(l_out));

    initial begin
        $dumpfile("mux_4_tb.vcd");
        $dumpvars;
        l_in0 = 1;
        l_in1 = 2;
        l_in2 = 3;
        l_in3 = 4;
        l_s = 0;
        #10
        assert(l_out === 1)

        l_in0 = 1;
        l_in1 = 2;
        l_in2 = 3;
        l_in3 = 4;
        l_s = 1;
        #10
        assert(l_out === 2)

        l_in0 = 1;
        l_in1 = 2;
        l_in2 = 3;
        l_in3 = 4;
        l_s = 2;
        #10
        assert(l_out === 3)

        l_in0 = 1;
        l_in1 = 2;
        l_in2 = 3;
        l_in3 = 4;
        l_s = 3;
        #10
        assert(l_out === 4)
        $finish;
    end
endmodule