#_____________________________________________________________________________
# Binary Adder
# Author: Alexander Kindall: CS 1400, Team 5(Alex, Sam, Dawson, Brian)
#-----------------------------------------------------------------------------
def convert(l,s):#Function to convert binary numbers to decimal
    d = 0
    for j in range(len(l)):
        if l[j] == "1":
            d = d + s
        s = s * 2#multiplies binary slot by 2
        if l[j] != "1" and l[j] != "0":#check if the binary number contains anything other than 1 or 0
            print("Not a binary number, cannot continue!")
            exit()#if contains something other than 1 or 0 end the code
    return d

#getting input
Bin1 = input("Give me 1 binary number: ")
Bin2 = input("Give me a binary number you want to add to the first: ")
b1 = []
b2 = []
#uploading input into lists element by element
for i in Bin1:
    b1.append(i)
for i in Bin2:
    b2.append(i)

#Reverses the lists so we can read binary from left to right
b1.reverse()
b2.reverse()
#set up variables
sclr = 1 #sclr is the value of each binary slot, starting at 1


Dec1 = convert(b1, sclr)
Dec2 = convert(b2, sclr)

Dec3 = Dec1 + Dec2#add the two original decimal values into a 3rd value
slot = 0#a variable that takes care of how many slots needed in a list to make the binary value of Dec3
while(sclr <= Dec3):
    sclr = sclr*2
    slot = slot +1
    
sclr = sclr/2

b3 = [None] * slot#creates a list that is the lenght of the slots we need, and contains arbitrary values(None)
for i in range(slot):
    if  (Dec3 // sclr)%2 == 0:
        b3[i] = '0'
        Dec3 = Dec3-sclr
        sclr = sclr/2
    else:
        b3[i] = '1'
        sclr = sclr/2
    
b1.reverse()
b2.reverse()
Bin3 = ''#changes list into a string that can be printed out nicely
for x in b3:#runs a loop through each element of b3 list
    Bin3 += ''+x#adds each element of b3 to Bin3 seperated by ''

print(Bin1, "+", Bin2, "=", Bin3)
