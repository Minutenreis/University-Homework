/**
 *N Bit Adder
 **/
module adder #(parameter N=64) (input  logic    [N-1:0] i_a,
                                                i_b,
                                input  logic    i_carry_in,
                                output logic    [N-1:0] o_s,
                                output logic    o_carry_out );
    assign {o_carry_out,o_s} = i_a + i_b + i_carry_in;

endmodule