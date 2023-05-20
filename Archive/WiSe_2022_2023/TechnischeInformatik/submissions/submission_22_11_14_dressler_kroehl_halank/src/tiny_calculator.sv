/**
 * Top-level entry of the tiny calculator.
 * The calculator adds the 4-bit binary numbers in SW[3:0] and SW[7:4].
 * The two inputs are shown on displays HEX0 and HEX1.
 * The result of the addition is shown on displays HEX2 and HEX3.
 *
 * @param SW bits of switch buttons SW7, SW6, SW5, SW4, SW3, SW2, SW1 and SW0.
 * @param HEX0 output bits which drive the seven-segment display HEX0.
 * @param HEX1 output bits which drive the seven-segment display HEX1.
 * @param HEX2 output bits which drive the seven-segment display HEX2.
 * @param HEX3 output bits which drive the seven-segment display HEX3.
 **/
module tiny_calculator( input  logic [7:0] SW,
                        output logic [6:0] HEX0,
                        output logic [6:0] HEX1,
                        output logic [6:0] HEX2,
                        output logic [6:0] HEX3 );
    logic [4:0] SUM; //sum
    ripple_carry_adder_4 m_dut( .i_a(SW[3:0]), .i_b(SW[7:4]), .i_carry_in(1'b0), .o_s(SUM[3:0]), .o_carry_out(SUM[4]) );
    decoder m_decoder0( .i_binary_number(SW[3:0]), .o_display(HEX0));
    decoder m_decoder1( .i_binary_number(SW[7:4]), .o_display(HEX1));
    decoder m_decoder2( .i_binary_number(SUM[3:0]), .o_display(HEX2));
    decoder m_decoder3( .i_binary_number({3'b000,SUM[4]}), .o_display(HEX3));
endmodule