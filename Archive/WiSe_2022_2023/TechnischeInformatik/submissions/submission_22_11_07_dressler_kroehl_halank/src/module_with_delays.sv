module module_with_delays(   input logic i_a,
                    input logic i_b,
                    input logic i_c,
                    output logic o_d
                );
    timeunit 1ns; timeprecision 1ns;
    logic l_notc, l_anotc, l_bc;

    not #3 m_not_0(l_notc,i_c);
    and #3 m_and_0(l_anotc,l_notc,i_a);
    and #3 m_and_1(l_bc,i_b,i_c);
    or #3 m_or_0(o_d,l_anotc,l_bc);

endmodule