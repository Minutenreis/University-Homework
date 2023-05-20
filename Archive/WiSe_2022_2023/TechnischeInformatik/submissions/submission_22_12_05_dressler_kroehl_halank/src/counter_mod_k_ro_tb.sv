/**
 * Testbench of the modulo-k counter which has the rollover signal as output.
 **/
module counter_mod_k_ro_tb;
  logic l_clk;
  logic l_reset;

  logic l_roll_over;
  logic [2:0] l_k;
  assign l_k = 3'b100;

  // clock
  always begin
      l_clk <= 1;
      #5;
      l_clk <= 0;
      #5;
  end

  // reset
  initial
    begin
      l_reset <= 1;
      #4;
      l_reset <= 0;
    end

  counter_mod_k_ro #(.N(3)) dut( l_clk,
                                l_reset,
                                l_k,
                                l_roll_over );

   initial begin
    $dumpfile("dump_counter_mod_k_ro.vcd");
    $dumpvars;

    #5;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b1 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b0 );
    #10;
    assert( l_roll_over === 1'b1 );
    #10;
    assert( l_roll_over === 1'b0 )
    #10;
  
    $finish;
  end
endmodule