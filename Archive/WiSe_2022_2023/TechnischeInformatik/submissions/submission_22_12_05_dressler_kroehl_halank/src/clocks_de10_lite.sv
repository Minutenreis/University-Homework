/**
 * Top-level module of the custom clocks.
 * The module displays a 10Hz clock signal through LEDR5, a 1Hz signal through LEDR6, and a 0.1Hz signal through LEDR7.
 * Switch button SW0 resets all resettable modules on low.
 *
 * @param MAX10_CLK1_50 MAX10_CLK1_50 clock signal available in the MAX 10 FPGA.
 * @param SW bits of ten switch buttons SW9 - SW0.
 * @param LEDR output bits corresponding to the board's ten leds LEDR9 - LEDR0.
 **/
module clocks_de10_lite( input  logic       MAX10_CLK1_50,
                         input  logic [9:0] SW,
                         output logic [9:0] LEDR );
  
  // Instantiate the clocks logical wires
  logic l_Ro_0_1, l_Ro_1, l_Ro_10;
  logic l_clk, l_reset;
  logic l_led_5, l_led_6, l_led_7;
  logic l_clk_0_1, l_clk_1, l_clk_10;

  // Connect Inputs
  assign l_clk = MAX10_CLK1_50;
  assign l_reset  = SW[1:0];

  // Instantiate Constants
  logic [27:0] l_k_0_1 = 25*10**7;
  logic [24:0] l_k_1 = 25*10**6;
  logic [21:0] l_k_10 = 25*10**5;

  // convert clock signals
  counter_mod_k_ro #(.N(28)) counter_mod_k_ro_0_1(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_0_1), .o_roll_over(l_Ro_0_1));
  counter_mod_k_ro #(.N(25)) counter_mod_k_ro_1(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_1), .o_roll_over(l_Ro_1));
  counter_mod_k_ro #(.N(22)) counter_mod_k_ro_10(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_10), .o_roll_over(l_Ro_10));

  clock clock_0_1(.i_roll_over(l_Ro_0_1), .i_reset(l_reset), .o_clk(l_clk_0_1));
  clock clock_1(.i_roll_over(l_Ro_1), .i_reset(l_reset), .o_clk(l_clk_1));
  clock clock_10(.i_roll_over(l_Ro_10), .i_reset(l_reset), .o_clk(l_clk_10));

  // Connect Outputs
  assign LEDR[5:5] = l_clk_10;
  assign LEDR[6:6] = l_clk_1;
  assign LEDR[7:7] = l_clk_0_1;
endmodule