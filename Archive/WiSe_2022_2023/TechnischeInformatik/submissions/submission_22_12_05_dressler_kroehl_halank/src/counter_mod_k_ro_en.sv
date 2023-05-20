/**
 * Counter which has the rollover signal as output.
 * The signal o_roll_over is high in every clock cycle after a rollover occurred and low in all other cycles.
 *
 * Assume k=3, then:
 * cycle     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | ...
 * mod k     | 0 | 1 | 2 | 0 | 1 | 2 | 0 | 1 | 2 | 0 |  1 | ...
 * rollover: | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |  0 | ...
 *
 *
 * @param i_clk input clock.
 * @param i_reset reset signal which resets the counter's value to zero.
 * @param i_k value k which is used for the modulo computation.
 * @param o_roll_over set to rollover signal which is high in every clock cycle after a rollover occurred; low else.
 **/
module counter_mod_k_ro_en #(parameter N=8) ( input  logic         i_clk,
                                           input  logic         i_reset,
                                           input  logic [N-1:0] i_k,
                                           input  logic         i_en,
                                           output logic         o_roll_over );
  // value of the counter
  logic [N-1:0] m_count;
  always_ff @(posedge i_clk, posedge i_reset)
  begin
    if(i_reset == 1'b1 )
      begin
        m_count <= {N{1'b0}};
        o_roll_over <= 1'b0;
      end
    else
      begin
        if(i_en==1)
            begin
                if( m_count == i_k-1 )
                    begin
                        m_count <= {N{1'b0}};
                        o_roll_over <= 1'b1;
                    end
                else
                    begin
                        m_count <= m_count + 1;
                        o_roll_over <= 1'b0;
                    end 
            end
      end
  end

endmodule