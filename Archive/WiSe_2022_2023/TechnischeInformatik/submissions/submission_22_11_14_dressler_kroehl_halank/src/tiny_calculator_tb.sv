/**
 * Testbench for Tiny Calculator
 */
module tiny_calculator_tb;
    logic [7:0] l_sw;
    logic [6:0] l_hex0, l_hex1, l_hex2, l_hex3;

    tiny_calculator m_dut(.SW(l_sw), .HEX0(l_hex0), .HEX1(l_hex1), .HEX2(l_hex2), .HEX3(l_hex3));

    initial begin
        $dumpfile("tiny_calculator_tb.vcd");
        $dumpvars;
        
        //general schema: l_sw = 8'bBBBB_AAAA
        //l_hex0 = A
        //l_hex1 = B
        //l_hex2 = C (4 least significant bits)
        //l_hex3 = C (most significant bit)

        l_sw = 8'b0000_0000; // 0 + 0 = 0
        #100;
        assert(l_hex0 == 7'b100_0000);
        assert(l_hex1 == 7'b100_0000);
        assert(l_hex2 == 7'b100_0000);
        assert(l_hex3 == 7'b100_0000);

        l_sw = 8'b0010_0011; // 2 + 3 = 5
        #100;
        assert(l_hex0 == 7'b011_0000);
        assert(l_hex1 == 7'b010_0100);
        assert(l_hex2 == 7'b001_0010);
        assert(l_hex3 == 7'b100_0000);

        l_sw = 8'b0001_0111; // 1 + 7 = 8
        #100;
        assert(l_hex0 == 7'b111_1000);
        assert(l_hex1 == 7'b111_1001);
        assert(l_hex2 == 7'b000_0000);
        assert(l_hex3 == 7'b100_0000);

        l_sw = 8'b1000_1000; // 8 + 8 = 16
        #100;
        assert(l_hex0 == 7'b000_0000);
        assert(l_hex1 == 7'b000_0000);
        assert(l_hex2 == 7'b100_0000);
        assert(l_hex3 == 7'b111_1001);

        l_sw = 8'b1111_1111; // 15 + 15 = 30 = 16 + 14
        #100;
        assert(l_hex0 == 7'b000_1110);
        assert(l_hex1 == 7'b000_1110);
        assert(l_hex2 == 7'b000_0110);
        assert(l_hex3 == 7'b111_1001);
        $finish;
    end
endmodule