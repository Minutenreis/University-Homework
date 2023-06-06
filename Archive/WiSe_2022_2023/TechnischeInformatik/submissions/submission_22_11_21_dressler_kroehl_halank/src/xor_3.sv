/**
 *3 Input xor (because we don't use bitwise operators apperantly)
 **/
module xor_3 ( input  logic i_in0,
                            i_in1,
                            i_in2,
               output logic o_res );
    logic l_xor0;
    xor xor_0 (l_xor0, i_in0, i_in1);
    xor xor_1 (o_res, l_xor0, i_in2);
endmodule