//___________________________________________________________________
// Falling Edge Flip Flop (D FF) code
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson)
//___________________________________________________________________
module FallingEdge_DFlipFlop(D,clk,Q); 
input D; // data 
input clk; // clock signal 
output reg clk; // output Q
always @(negedge clk) 
begin 
    Q <= D; 
end 
endmodule 
