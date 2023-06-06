/**
 *Testbench for decoder_2_4
 **/
module decoder_2_4_tb;
    logic [1:0] l_binary;
    logic [3:0] l_one_hot;

    decoder_2_4 m_dut(.i_binary(l_binary), .o_one_hot(l_one_hot));

    initial begin
        $dumpfile("decoder_2_4_tb.vcd");
        $dumpvars;

        l_binary = 2'b00;
        #10
        assert(l_one_hot === 4'b0001)

        l_binary = 2'b01;
        #10
        assert(l_one_hot === 4'b0010)

        l_binary = 2'b10;
        #10
        assert(l_one_hot === 4'b0100)

        l_binary = 2'b11;
        #10
        assert(l_one_hot === 4'b1000)

        $finish;
    end
endmodule