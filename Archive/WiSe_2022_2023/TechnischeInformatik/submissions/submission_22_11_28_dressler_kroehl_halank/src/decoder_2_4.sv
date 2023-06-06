/**
2 bit input 4 bit output decoder
@param i_binary 2 bit input
@param o_one_hot 4 bit output output
*/
module decoder_2_4( input  logic [1:0] i_binary,
                    output logic [3:0] o_one_hot );
    always_comb begin
        case (i_binary)
            2'b00: o_one_hot = 4'b0001;
            2'b01: o_one_hot = 4'b0010;
            2'b10: o_one_hot = 4'b0100;
            2'b11: o_one_hot = 4'b1000;
            default: o_one_hot = 4'bxxxx;
        endcase
    end
        

endmodule
    