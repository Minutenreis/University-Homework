/**
 *4er Mux für N bits
 **/
module mux_4 #(parameter N=64) (input  logic [N-1:0]    i_in0,
                                                        i_in1,
                                                        i_in2,
                                                        i_in3,
                                input  logic [1:0]      i_s,
                                output logic [N-1:0]    o_out );
    logic [N-1:0] l_out0;
    logic [N-1:0] l_out1;

    mux_2 #(.N(N)) mux_2_0 ( .i_in0 ( i_in0 ),
                            .i_in1 ( i_in1 ),
                            .i_s   ( i_s[0] ),
                            .o_out ( l_out0 ) );

    mux_2 #(.N(N)) mux_2_1 ( .i_in0 ( i_in2 ),
                            .i_in1 ( i_in3 ),
                            .i_s   ( i_s[0] ),
                            .o_out ( l_out1 ) );

    mux_2 #(.N(N)) mux_2_2 ( .i_in0 ( l_out0 ),
                            .i_in1 ( l_out1 ),
                            .i_s   ( i_s[1] ),
                            .o_out ( o_out ) );
endmodule