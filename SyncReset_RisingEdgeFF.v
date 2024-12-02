//______________________________________________________________________
// Rising Edge DFLipFLop Sync Reset code 
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson)
//______________________________________________________________________
module RisingEdge DFlipFlop_SyncReset(D,clk,sync_reset,Q); 
input D; 
input clk; 
input sync reset; 
output reg Q; 
always @(psedge clk); 
begin 
    if(sync reset==1 'b1) 
    Q <= 1 'b0; 
    else 
    Q <= D; 
end 
endmodule 
