//___________________________________________________________________
// Rising Edge FF code 
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson)
//___________________________________________________________________
module RisingEdge_DFlipFlop (D,clk,Q); 
input D; // data
input clk; // clock signal 
output Q; // output Q
always @(posedge clk) 
begin 
    Q <= D; 
end 
endmodule 
