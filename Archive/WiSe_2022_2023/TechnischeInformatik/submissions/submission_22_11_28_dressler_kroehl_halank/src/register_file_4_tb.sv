/**
 * Testbench of the 4-bit register file.
 **/
module register_file_4_tb;
  logic       l_clk;
  logic [1:0] l_reg_read_0, l_reg_read_1;
  logic [1:0] l_reg_write;
  logic [3:0] l_port_write;
  logic       l_write_enable;
  logic [3:0] l_port_read_0;
  logic [3:0] l_port_read_1;

  // clock
  always
  begin
    l_clk <= 1;
    #5;
    l_clk <= 0;
    #5;
  end

  register_file_4 m_dut( .i_clk(          l_clk          ),
                         .i_reg_read_0(   l_reg_read_0   ),
                         .i_reg_read_1(   l_reg_read_1   ),
                         .i_reg_write(    l_reg_write    ),
                         .i_port_write(   l_port_write   ),
                         .i_write_enable( l_write_enable ),
                         .o_port_read_0(  l_port_read_0  ),
                         .o_port_read_1(  l_port_read_1  ) );

  initial
  begin
    $dumpfile("dump_register_file_4.vcd");
    $dumpvars;
    #5;
    l_reg_read_0   = 2'b00;
    l_reg_read_1   = 2'b00;
    l_reg_write    = 2'b00;
    l_port_write   = 4'b1010;
    l_write_enable = 1'b1;
    #10;
    // current internal status
    //   reg 00: 1010
    //   reg 01: xxxx
    //   reg 10: xxxx
    //   reg 11: xxxx
    assert( l_port_read_0 === 4'b1010 );
    assert( l_port_read_1 === 4'b1010 );
    #1;

    l_reg_read_0   = 2'b10;
    l_reg_read_1   = 2'b00;
    l_reg_write    = 2'b10;
    l_port_write   = 4'b1110;
    l_write_enable = 1'b1;
    #9;
    // current internal status
    //   reg 00: 1010
    //   reg 01: xxxx
    //   reg 10: 1110
    //   reg 11: xxxx
    assert( l_port_read_0 === 4'b1110 );
    assert( l_port_read_1 === 4'b1010 );
    #1;

    l_reg_read_0   = 2'b10;
    l_reg_read_1   = 2'b10;
    l_reg_write    = 2'b11;
    l_port_write   = 4'b1111;
    l_write_enable = 1'b1;
    #9;
    // current internal status
    //   reg 00: 1010
    //   reg 01: xxxx
    //   reg 10: 1110
    //   reg 11: 1111
    assert( l_port_read_0 === 4'b1110 );
    assert( l_port_read_1 === 4'b1110 );
    #1;

    l_reg_read_0   = 2'b11;
    l_reg_read_1   = 2'b00;
    l_reg_write    = 2'b00;
    l_port_write   = 4'b1000;
    l_write_enable = 1'b1;
    #9;
    // current internal status
    //   reg 00: 1000
    //   reg 01: xxxx
    //   reg 10: 1110
    //   reg 11: 1111
    assert( l_port_read_0 === 4'b1111 );
    assert( l_port_read_1 === 4'b1000 );
    #1;

    l_reg_read_0   = 2'b11;
    l_reg_read_1   = 2'b00;
    l_reg_write    = 2'b00;
    l_port_write   = 4'b0000;
    l_write_enable = 1'b0;
    #9;
    // current internal status
    //   reg 00: 1000
    //   reg 01: xxxx
    //   reg 10: 1110
    //   reg 11: 1111
    assert( l_port_read_0 === 4'b1111 );
    assert( l_port_read_1 === 4'b1000 );
    #1;

    $finish;
  end


endmodule
