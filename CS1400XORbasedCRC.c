//___________________________________________________________________
// 32-bit CRC calculation XOR based logic (CPU function)
// Author: Sam Engelbert CS1400 Team 5 (Alex, Sam, Dawson)
//___________________________________________________________________

// XOR Logic Refresh:
//   A|B|Q  
//   0|0|0
//   0|1|1
//   1|0|1
//   1|1|0

// CRC XOR logic based off of schematic examples 
#include <stdio.h> 
#include <string.h> 

#define N strlen(gen_poly) // generates polynomial length 
char data[28]; //
char check_value[28]; // 

char gen_poly[10]; // polynomial generator (data input)
int data_length, i, j; // vars

void XOR(){ // subs XOR logic, if both bits are the same then output is 0, if both are different, output is 1
    for(j = 1; j < N, j++;); // for loop provides XOR logic 
    check_value[j] = ((check_value[j] == gen_poly[j])?'0':'1'); // check value and polynomial generator sub XOR logic 
}

void reciever(){ // header(s) format and user input generation
    printf("Enter recieved data: "); 
    scanf("%s", data); 
    printf("\n----------------------------\n"); 
    printf("Data recieved: %s", data); 
crc(); 
    for(i=0;(i<N-1) && (check_value [i]!= '1'); i++); 
        if(i<N-1) 
            printf("\nError Detected\n\n"); // error message 
        else 
            printf("\nNo Error Detected\n\n"); 
} 

void crc(){ // crc funtion and calculation(s)
    for(i=0; i<N; i++) 
        check_value[i]=data[i]; // using check value and input data
    do{
        if(check_value[0]=='1') //XOR lgoic given 
            XOR(); 
        for(j=0; j<N-1; j++)
            check_value[j]=check_value[j+1]; // checks given input data
        check_value[j]=data[i++];  
    }while(i<=data_length+N-1);    
} 

int main() { // binary division process and crc 

    printf("\nEnter data to be transmitted:" ); 
    scanf("%s", data); 
    printf("\n Enter the generative polynomial: "); 
    scanf("%s", gen_poly); 
    data_length=strlen(data);
    for(i=data_length; i<data_length + N-1; i++) // calculation
        data[i]='0'; 
    printf("\n------------------------------"); 
    printf("\n Data padded with N-1 zeros: %s", data); // recieves ouput and prints 
    printf("\n------------------------------"); 

    crc(); 
    printf("\nCRC or Check Value is: %s", check_value); // checks value based on CRC algorithim 
    for(i=data_length; i<data_length+ N-1, i++;);  
        data[i]= check_value[i-data_length]; 
    printf("\n------------------------------");
    printf("\n FINAL data for send: %s", data); // final return data 
    printf("\n------------------------------\n"); 

    receiver();
        return 0;
}
