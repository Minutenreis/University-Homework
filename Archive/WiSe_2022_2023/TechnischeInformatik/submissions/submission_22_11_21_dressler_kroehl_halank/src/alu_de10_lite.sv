/**
 * Top-level module of the basic alu.
 * The alu operates on the 4-bit binary numbers in SW[3:0] and SW[7:4].
 * The two input numbers are shown on displays HEX0 and HEX1.
 * The control signal is shown using LEDR1 and LEDR0.
 * The result is shown on display HEX2.
 * The carry out is shown via LEDR7.
 *
 * @param SW bits of ten switch buttons SW9 - SW0.
 * @param LEDR output bits corresponding to the board's ten leds LEDR9 - LEDR0.
 * @param HEX0 output bits which drive the seven-segment display HEX0.
 * @param HEX1 output bits which drive the seven-segment display HEX1.
 * @param HEX2 output bits which drive the seven-segment display HEX2.
 **/
module alu_de10_lite(   input  logic [9:0] SW,
                        output logic [9:0] LEDR,
                        output logic [6:0] HEX0,
                        output logic [6:0] HEX1,
                        output logic [6:0] HEX2 );
    logic [1:0] l_alu_ctrl;
    logic [3:0] l_a;
    logic [3:0] l_b;
    logic [3:0] l_result;
    logic       l_carry_out;

    // "rename" inputs
    assign l_alu_ctrl[1:0] = SW[9:8];
    assign l_a[3:0] = SW[3:0];
    assign l_b[3:0] = SW[7:4];

    // alu
    alu #(.N(4)) m_alu( .i_a(l_a), .i_b(l_b), .i_alu_ctrl(l_alu_ctrl), .o_result(l_result), .o_carry_out(l_carry_out) );

    assign LEDR[1:0] = l_alu_ctrl[1:0];
    assign LEDR[7]   = l_carry_out;
    decoder decoder_1(.i_binary_number(l_a[3:0]), .o_display(HEX0));
    decoder decoder_2(.i_binary_number(l_b[3:0]), .o_display(HEX1));
    decoder decoder_0(.i_binary_number(l_result[3:0]), .o_display(HEX2));

endmodule