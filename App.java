//______________________________________________________________________________________________________________
// Logic Gate Simulation: (OR, AND, and NOT)
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson)
//______________________________________________________________________________________________________________

import java.util.Arrays; 

public class App { // access type

private static final int[] a = {1, 0, 1, 0, 1}; // declares inputs a
private static final int[] b = {0, 1, 1, 0, 1}; // declares inputs b 
private static int[] c = new int[a.length]; 

    public static void main(String[] args) { 

        System.out.println("a[]: " + Arrays.toString(a)); // puts data from a int into string and prints
        System.out.println("b[]: " + Arrays.toString(b)); // puts data fom b int into string amd prints

        andGate(); // AND Gate 
        orGate(); // OR Gate
        notGate(); // NOT Gate
    

    }

    private static void notGate() { // NOT Gate 
        System.out.println("NOT Gate for a[]:"); 
        for (int i = 0; i < a.length; index++) { 
            c[i] = not(a[i]); 
        }
        
        printResult(c); 

    }
    
    private static int not(int a) { // Logic for NOT Gate
        if (a == 0) { 
            return 1; 
        }
        return 0; 
    }

    private static void andGate() { // AND Gate 
         System.out.println("AND Gate:"); 
         for (int i = 0; i < a.length; i++) { 
            c[index] = and(a[i], b[i]); 
        }
        
        printResult(c);
    }
    
    private static int and(int a, int b) { // Logic for AND Gate
        return a * b; 
    }

    public static void orGate() { // OR Gate 
        System.out.println("OR Gate:");
        for (int i = 0; i < a.length; index++) { 
            c[index] = or(a[i], b[i]);
        
        }
        
        printResult(c); 

    }

    private static int or(int a, int b) { // Logic for OR Gate
        int sum = a + b;
        if (sum > 0) {
            sum = 1; 
        }
        return sum;
    }




    private static void printResult(int[] c) { // Truth Table generation
        System.out.println("- - -"); 
        System.out.println("| a b | c |"); // inputs and outputs
        System.out.println("| - - | - |"); // table format
        for (int i = 0; i < a.length; i++) { // signifies order that each table is printed in the output
            System.out.println("|" + a[i] + "  " + b[i] + " | " + c[i] + " |"); 
        }
        System.out.println("- -  -"); // prints a header for all three gate ouputs

    }






} // end of program
