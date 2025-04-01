module counter #(parameter DATA_SIZE) (
  input clk,
  input rst,
  output logic[DATA_SIZE-1:0] out
);

  always_ff @ (posedge clk) begin
    if (rst)
      out <= 0;
    else
      out <= out + 1;
  end
endmodule
