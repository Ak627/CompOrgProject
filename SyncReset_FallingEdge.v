//___________________________________________________________________
// Falling Edge DFlipFlop Sync Reset code
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson, and Brian)
//___________________________________________________________________ 
module FallingEdge_DFlipFlop_SyncReset(D,clk,sync_reset,Q); 
input D; 
input clk; 
input sync_reset; 
output reg Q; 
begin 
    if(sync_reset==1'b1) 
    Q <= 1'b0; 
    else
    Q <= D; 
end 
endmodule 

