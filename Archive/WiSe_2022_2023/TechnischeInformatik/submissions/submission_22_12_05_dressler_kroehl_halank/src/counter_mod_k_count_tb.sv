/**
 * Testbench of the modulo-k counter which has number of elapsed clock cycles as output.
 **/
module counter_mod_k_count_tb;
  logic l_clk;
  logic l_reset;

  logic [1:0] l_count;
  logic [1:0] l_k;
  assign l_k = 2'b11;

  // reset
  initial
    begin
      l_reset <= 1;
      #3;
      l_reset <= 0;
    end

  // clock
  always
    begin
      l_clk <= 1;
      #5;
      l_clk <= 0;
      #5;
    end

  counter_mod_k_count #(2) dut( l_clk,
                                l_reset,
                                l_k,
                                l_count );

  initial begin
    $dumpfile("dump_counter_mod_k_count.vcd");
    $dumpvars;

    #5;
    assert( l_count === 3'd0 );
    #10;
    assert( l_count === 3'd1 );
    #10;
    assert( l_count === 3'd2 );
    #10;
    assert( l_count === 3'd0 );
    #10;
    assert( l_count === 3'd1 );
    #10;
    assert( l_count === 3'd2 );
    #10;
    assert( l_count === 3'd0 );
    #10;
    assert( l_count === 3'd1 );
    #10;
    assert( l_count === 3'd2 );

    $finish;
  end
endmodule