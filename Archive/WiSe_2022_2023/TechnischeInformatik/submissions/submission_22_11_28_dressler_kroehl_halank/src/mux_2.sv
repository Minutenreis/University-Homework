/**
 *2er Mux für N bits
 **/
module mux_2 #(parameter N=64) ( input  logic [N-1:0] i_in0,
                                                   i_in1,
                              input  logic         i_s,
                              output logic [N-1:0] o_out );
    always_comb
    begin
        case(i_s)
            1'b0: o_out = i_in0;
            1'b1: o_out = i_in1;
            default: o_out = 1'bx;
        endcase
    end

endmodule