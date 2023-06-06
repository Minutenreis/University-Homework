/**
 * Testbench for 3 Input XOR Gate
 **/
module xor_3_tb;

    logic l_in0, l_in1, l_in2, l_res;

    xor_3 m_dut (.i_in0(l_in0), .i_in1(l_in1), .i_in2(l_in2), .o_res(l_res));

    initial begin
        $dumpfile("xor_3_tb.vcd");
        $dumpvars;

        l_in0 = 0;
        l_in1 = 0;
        l_in2 = 0;
        #10;
        assert(l_res === 0);

        l_in0 = 0;
        l_in1 = 0;
        l_in2 = 1;
        #10;
        assert(l_res === 1);

        l_in0 = 0;
        l_in1 = 1;
        l_in2 = 0;
        #10;
        assert(l_res === 1);

        l_in0 = 1;
        l_in1 = 0;
        l_in2 = 0;
        #10;
        assert(l_res === 1);

        l_in0 = 0;
        l_in1 = 1;
        l_in2 = 1;
        #10;
        assert(l_res === 0);

        l_in0 = 1;
        l_in1 = 0;
        l_in2 = 1;
        #10;
        assert(l_res === 0);

        l_in0 = 1;
        l_in1 = 1;
        l_in2 = 0;
        #10;
        assert(l_res === 0);

        l_in0 = 1;
        l_in1 = 1;
        l_in2 = 1;
        #10;
        assert(l_res === 1);
        $finish;
    end


endmodule