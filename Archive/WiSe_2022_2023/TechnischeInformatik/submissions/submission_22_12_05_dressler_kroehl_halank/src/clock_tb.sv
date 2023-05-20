/**
 * Testbench of the clock derived from a counter's rollover signal.
 **/
module clock_tb;
  logic l_reset;
  logic l_clk;
  logic l_roll_over;

  // reset
  initial
    begin
      l_reset <= 1;
      #4;
      l_reset <= 0;
    end

  // rollover T=#20
  always begin
      l_roll_over <= 1;
      #2;
      l_roll_over <= 0;
      #8;
  end

  //clock T=#20
  clock dut( .i_roll_over(l_roll_over),
             .i_reset(l_reset),
             .o_clk(l_clk) );

  initial begin
    $dumpfile("dump_clock.vcd");
    $dumpvars;

    #5;
    assert( l_clk === 1'b1 );
    #10;
    assert( l_clk === 1'b0 );
    #10;
    assert( l_clk === 1'b1 );
    #10;
    assert( l_clk === 1'b0 );
    #10;
    assert( l_clk === 1'b1 );
    #10;
    assert( l_clk === 1'b0 );
    #10;

    $finish;
  end
endmodule