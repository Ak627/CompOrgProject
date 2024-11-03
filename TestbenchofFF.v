//____________________________________________________________________
// Visual Testbench code for FF's
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson, and Brian)
//____________________________________________________________________
`timescale 1ns/1ps
module tb_DFF(); 
reg D; 
reg clk; 
reg reset; 
wire Q; 

RisingEdge_DFlipFlop_SyncReset dut(D,clk,reset,Q); 

    initial begin 
        clk = 0; 
            forever #10 clk = ~clk; 
    end 
    initial begin 
        reset=1; 
        #100; 
        reset=0; 
        D <= 1; 
        #100; 
        D<= 0; 
        #100; 
    end  
endmodule 