/**
 * Testbench of the gate-level module_with_delay
 */
module full_adder_tb;
    timeunit 1ns; timeprecision 1ns;
    logic l_a,l_b,l_c,l_d;

    module_with_delays m_dut( .i_a(l_a), .i_b(l_b), .i_c(l_c), .o_d(l_d));

    initial begin
        $dumpfile("dump_module_with_delay.vcd");
        $dumpvars;

        l_a = 1'b1;
        l_b = 1'b1;
        l_c = 1'b1;
        #10
        l_a = 1'b1;
        l_b = 1'b1;
        l_c = 1'b0;
        #10
    
        $finish;
    end
endmodule