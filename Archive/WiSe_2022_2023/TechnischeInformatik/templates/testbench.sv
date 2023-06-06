/**
 *Testbench for <name>
 **/
module <name>_tb;
    <name> m_dut();

    initial begin
        $dumpfile("<name>_tb.vcd");
        $dumpvars;



        $finish;
    end
endmodule