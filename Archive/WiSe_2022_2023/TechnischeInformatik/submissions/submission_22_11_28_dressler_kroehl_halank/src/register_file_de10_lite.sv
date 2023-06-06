/**
 * Top-level module of the 4-bit register file:
 *   - switch buttons 0-1 set the register connected to read port 0.
 *   - switch buttons 2-3 set the register connected to read port 1.
 *   - switch buttons 4-5 set the register to which data is written.
 *   - switch buttons 6-9 set the data at the write port.
 *   - push button 0 asserts the write enable signal if pushed.
 *
 *   - hex0 shows the id of the register connected to read port 0.
 *   - hex1 shows the id of the register connected to read port 1.
 *   - hex2 shows the id of the register connected to the write port.
 *   - hex3 shows the data at the write port.
 *   - hex4 shows the data at the first read port.
 *   - hex5 shows the data at the second read port.
 *   - ledr0 shows the write enable signal.
 *
 * @param MAX10_CLK1_50 clock signal available in the MAX 10 FPGA.
 * @param KEY data of the push buttons.
 * @param SW data of the switch buttons.
 * @param HEX0 output bits which drive the seven-segment display HEX0.
 * @param HEX1 output bits which drive the seven-segment display HEX1.
 * @param HEX2 output bits which drive the seven-segment display HEX2.
 * @param HEX3 output bits which drive the seven-segment display HEX3.
 * @param HEX4 output bits which drive the seven-segment display HEX4.
 * @param HEX5 output bits which drive the seven-segment display HEX5.
 * @param LEDR output bits which drive the ten leds.
 **/
module register_file_de10_lite( input  logic       MAX10_CLK1_50,
                                input  logic [1:0] KEY,
                                input  logic [9:0] SW,
                                output logic [6:0] HEX0,
                                                   HEX1,
                                                   HEX2,
                                                   HEX3,
                                                   HEX4,
                                                   HEX5,
                                output logic [0:9] LEDR );
  logic [1:0] l_reg_read_0, l_reg_read_1, l_reg_write;
  logic [3:0] l_port_write, l_port_read_0, l_port_read_1;
  logic [0:0] l_write_enable, l_clk;

  // Connect Inputs
  assign l_reg_read_0  = SW[1:0];
  assign l_reg_read_1  = SW[3:2];
  assign l_reg_write   = SW[5:4];
  assign l_port_write  = SW[9:6];
  assign l_write_enable = !KEY[0:0];
  assign l_clk = MAX10_CLK1_50;

  // Instantiate the register file
  register_file_4 reg_file( .i_clk(l_clk),
                            .i_reg_read_0(l_reg_read_0),
                            .i_reg_read_1(l_reg_read_1),
                            .i_reg_write(l_reg_write),
                            .i_port_write(l_port_write),
                            .i_write_enable(l_write_enable),
                            .o_port_read_0(l_port_read_0),
                            .o_port_read_1(l_port_read_1));

  // Connect Outputs
  decoder dec0( .i_binary_number({2'b00,l_reg_read_0}), .o_display(HEX0) );
  decoder dec1( .i_binary_number({2'b00,l_reg_read_1}), .o_display(HEX1) );
  decoder dec2( .i_binary_number({2'b00,l_reg_write}),  .o_display(HEX2) );
  decoder dec3( .i_binary_number(l_port_write), .o_display(HEX3) );
  decoder dec4( .i_binary_number(l_port_read_0), .o_display(HEX4) );
  decoder dec5( .i_binary_number(l_port_read_1), .o_display(HEX5) );
  assign LEDR[0:0] = l_write_enable;

endmodule
