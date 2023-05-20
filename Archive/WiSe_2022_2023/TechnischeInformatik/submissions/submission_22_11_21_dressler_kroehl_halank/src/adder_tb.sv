/**
 *Testbench for N-Bit adder
 **/

module adder_tb;
    logic [63:0] l_a, l_b, l_s;
    logic l_carry_in, l_carry_out;

    adder #(.N(64)) m_dut(.i_a(l_a), .i_b(l_b), .i_carry_in(l_carry_in), .o_s(l_s), .o_carry_out(l_carry_out));

    initial begin
        $dumpfile("adder_tb.vcd");
        $dumpvars;
        l_a = 0;
        l_b = 0;
        l_carry_in = 0;
        #100;
        assert(l_s === 0);
        assert(l_carry_out === 0);

        l_a = 1;
        l_b = 0;
        l_carry_in = 0;
        #100;
        assert(l_s === 1);
        assert(l_carry_out === 0);

        l_a = 0;
        l_b = 0;
        l_carry_in = 1;
        #100;
        assert(l_s === 1);
        assert(l_carry_out === 0);

        l_a = 2**64-1;
        l_b = 2**64-1;
        l_carry_in = 1;
        #100;
        assert(l_s === 2**64-1);
        assert(l_carry_out === 1);

        l_a = 2**64-1;
        l_b = 0;
        l_carry_in = 1;
        #100;
        assert(l_s === 0);
        assert(l_carry_out === 1);

        $finish;
    end
endmodule