/**
 * Gate-level implementation of a full adder.
 *
 * @param i_a input A.
 * @param i_b input B.
 * @param i_carry_in carry in.
 * @param o_s sum.
 * @param o_carry_out carry out.
 **/
module full_adder( input  logic i_a,
                                i_b,
                                i_carry_in,
                   output logic o_s,
                                o_carry_out );

    logic l_ab, l_bc, l_ca;
    xor m_xor_0( o_s, i_a, i_b, i_carry_in );
    and m_and_0( l_ab, i_a, i_b );
    and m_and_1( l_bc, i_b, i_carry_in );
    and m_and_2( l_ca, i_carry_in, i_a );
    or m_or_0( o_carry_out, l_ab, l_bc, l_ca );
endmodule