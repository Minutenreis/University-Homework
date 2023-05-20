module my_module_tb;
    logic l_a, l_b, l_c;

    my_module m_dut( .i_a(l_a), .i_b(l_b), .o_c(l_c) );

    initial begin
        $dumpfile("dump_my_module.vcd");
        $dumpvars;

        l_a = 1'b0;
        l_b = 1'b0;
        #10;
        assert(l_c === 1'b1);

        l_a = 1'b0;
        l_b = 1'b1;
        #10;
        assert(l_c === 1'b1);

        l_a = 1'b1;
        l_b = 1'b0;
        #10;
        assert(l_c === 1'b0);

        l_a = 1'b1;
        l_b = 1'b1;
        #10;
        assert(l_c === 1'b1);

        $finish;
    end
endmodule