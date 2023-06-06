module my_module(   input logic i_a,
                    input logic i_b,
                    output logic o_c
                );
    logic l_x;

    not m_gate_0( l_x, i_a);
    or m_gate_1( o_c, l_x, i_b);
endmodule