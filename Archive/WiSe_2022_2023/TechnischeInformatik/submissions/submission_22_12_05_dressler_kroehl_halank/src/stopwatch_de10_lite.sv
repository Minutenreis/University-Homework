/**
 * Stopwatch Component for DE10-lite board
 * @param MAX10_CLK1_50 MAX10_CLK1_50 clock signal available in the MAX 10 FPGA.
 * @param SW bits of ten switch buttons SW9 - SW0.
 * @param LEDR output bits corresponding to the board's ten leds LEDR9 - LEDR0.
 * @param HEX
 **/
module stopwatch_de10_lite( input logic         MAX10_CLK1_50,
                            input logic [9:0]   SW, //Switches
                            input logic [1:0]   KEY, //Active Low
                            output logic [9:0]  LEDR, //Active High
                            output logic [6:0]  HEX0, //Active Low
                                                HEX1,
                                                HEX2,
                                                HEX3,
                                                HEX4,
                                                HEX5);

    // Instantiate the stopwatches logical wires
    logic l_Ro_10s, l_Ro_1s, l_Ro_0_1s, l_Ro_1m, l_Ro_10m;
    logic l_clk_10m, l_clk_1m, l_clk_0_1s, l_clk_1s, l_clk_10s;
    logic [2:0] l_count_10m, l_count_10s;
    logic [3:0] l_count_1m, l_count_0_1s, l_count_1s;
    logic l_clk, l_reset, l_en;

    // Connect Inputs
    assign l_clk = MAX10_CLK1_50;
    assign l_reset = ~KEY[0];
    assign l_en = SW[0];

    // Instantiate Constants
    logic [33:0] l_k_10m = 15*10**9;
    logic [30:0] l_k_1m = 15*10**8;
    logic [27:0] l_k_10s = 25*10**7;
    logic [24:0] l_k_1s = 25*10**6;
    logic [21:0] l_k_0_1s = 25*10**5;

    // Instantiate the stopwatch
    counter_mod_k_ro_en #(.N(34)) counter_mod_k_ro_10m(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_10m), .i_en(l_en), .o_roll_over(l_Ro_10m));
    counter_mod_k_ro_en #(.N(31)) counter_mod_k_ro_1m(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_1m), .i_en(l_en), .o_roll_over(l_Ro_1m));
    counter_mod_k_ro_en #(.N(28)) counter_mod_k_ro_10s(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_10s), .i_en(l_en), .o_roll_over(l_Ro_10s));
    counter_mod_k_ro_en #(.N(25)) counter_mod_k_ro_1s(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_1s), .i_en(l_en), .o_roll_over(l_Ro_1s));
    counter_mod_k_ro_en #(.N(22)) counter_mod_k_ro_0_1s(.i_clk(l_clk), .i_reset(l_reset), .i_k(l_k_0_1s), .i_en(l_en), .o_roll_over(l_Ro_0_1s));

    clock clock_10m(.i_roll_over(l_Ro_10m), .i_reset(l_reset), .o_clk(l_clk_10m));
    clock clock_1m(.i_roll_over(l_Ro_1m), .i_reset(l_reset), .o_clk(l_clk_1m));
    clock clock_10s(.i_roll_over(l_Ro_10s), .i_reset(l_reset), .o_clk(l_clk_10s));
    clock clock_1s(.i_roll_over(l_Ro_1s), .i_reset(l_reset), .o_clk(l_clk_1s));
    clock clock_0_1s(.i_roll_over(l_Ro_0_1s), .i_reset(l_reset), .o_clk(l_clk_0_1s));

    counter_mod_k_count_en #(.N(3)) counter_10m(.i_clk(l_clk_10m), .i_k(3'b110), .i_reset(l_reset), .i_en(l_en), .o_count(l_count_10m));
    counter_mod_k_count_en #(.N(4)) counter_1m(.i_clk(l_clk_1m), .i_k(4'b1010), .i_reset(l_reset), .i_en(l_en), .o_count(l_count_1m));
    counter_mod_k_count_en #(.N(3)) counter_10s(.i_clk(l_clk_10s), .i_k(3'b110), .i_reset(l_reset), .i_en(l_en), .o_count(l_count_10s));
    counter_mod_k_count_en #(.N(4)) counter_1s(.i_clk(l_clk_1s), .i_k(4'b1010), .i_reset(l_reset), .i_en(l_en), .o_count(l_count_1s));
    counter_mod_k_count_en #(.N(4)) counter_0_1s(.i_clk(l_clk_0_1s), .i_k(4'b1010), .i_reset(l_reset), .i_en(l_en), .o_count(l_count_0_1s));

    // Connect Outputs 7 Segment Displays
    decoder decoder_10m(.i_binary_number({1'b0,l_count_10m}), .o_display(HEX5));
    decoder decoder_1m(.i_binary_number(l_count_1m), .o_display(HEX4));
    assign HEX3 = {l_Ro_1s,6'b111111}; //blinking dash
    decoder decoder_10s(.i_binary_number({1'b0,l_count_10s}), .o_display(HEX2));
    decoder decoder_1s(.i_binary_number(l_count_1s), .o_display(HEX1));
    decoder decoder_0_1s(.i_binary_number(l_count_0_1s), .o_display(HEX0));

    // Connect Outputs LEDs
    assign LEDR[9] = l_Ro_10m;
    assign LEDR[8] = l_Ro_1m;
    assign LEDR[7] = l_Ro_10s;
    assign LEDR[6] = l_Ro_1s;
    assign LEDR[5] = l_Ro_0_1s;

endmodule