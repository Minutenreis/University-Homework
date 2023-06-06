/**
 * Counter which has the number of elapsed clock cycles modulo k as output.
 *
 * @param i_clk input clock.
 * @param i_reset reset signal which resets the counter's value to zero.
 * @param i_k value k which is used for the modulo computation.
 * @param o_count set to number of elapsed clock cycles modulo k.
 **/
module counter_mod_k_count_en #(parameter N=8) ( input  logic         i_clk,
                                              input  logic         i_reset,
                                              input  logic [N-1:0] i_k,
                                              input logic         i_en,
                                              output logic [N-1:0] o_count );
  // current value of the counter
  logic [N-1:0] m_count;

  // on positive edge of input clock or reset
  // either reset counter or assign next value
  always_ff @(posedge i_clk, posedge i_reset)
    begin
      if( i_reset == 1'b1 )
        begin
          m_count <= {N{1'b0}};
        end
      else
        begin
            if(i_en == 1'b1)
                begin
                    if( m_count == i_k-1 )
                        begin
                            m_count <= {N{1'b0}};
                        end
                    else
                        begin
                            m_count <= m_count + 1;
                        end
                end
        end
    end

  // assign output bus
  assign o_count = m_count;
endmodule