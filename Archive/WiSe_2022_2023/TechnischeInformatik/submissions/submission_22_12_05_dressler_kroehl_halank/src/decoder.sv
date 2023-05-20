/**
 * Decoder for a seven-segment display.
 *
 * @param i_binary_number input binary number.
 * @param o_display output bits driving the seven-segment display.
 **/
module decoder( input  logic [3:0] i_binary_number,
                output logic [6:0] o_display );
  always_comb
  begin
    case( i_binary_number )
        4'b0000: o_display[6:0] = 7'b100_0000; // 0
        4'b0001: o_display[6:0] = 7'b111_1001; // 1
        4'b0010: o_display[6:0] = 7'b010_0100; // 2
        4'b0011: o_display[6:0] = 7'b011_0000; // 3
        4'b0100: o_display[6:0] = 7'b001_1001; // 4
        4'b0101: o_display[6:0] = 7'b001_0010; // 5
        4'b0110: o_display[6:0] = 7'b000_0010; // 6
        4'b0111: o_display[6:0] = 7'b111_1000; // 7
        4'b1000: o_display[6:0] = 7'b000_0000; // 8
        4'b1001: o_display[6:0] = 7'b001_0000; // 9
        4'b1010: o_display[6:0] = 7'b000_1000; // A
        4'b1011: o_display[6:0] = 7'b000_0011; // B
        4'b1100: o_display[6:0] = 7'b100_0110; // C
        4'b1101: o_display[6:0] = 7'b010_0001; // D
        4'b1110: o_display[6:0] = 7'b000_0110; // E
        4'b1111: o_display[6:0] = 7'b000_1110; // F
        default: o_display[6:0] = 7'bxxx_xxxx;
    endcase
  end
endmodule