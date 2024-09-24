#getting input
Bin1 = input("Give me 1 binary number: ")
Bin2 = input("Give me a binary number you want to add to the first: ")
b1 = []
b2 = []
#uploading input into lists, converting to strings
for i in Bin1:
    b1.append(i)
for i in Bin2:
    b2.append(i)
#Reverses the lists so we can read binary from left to right
b1.reverse()
b2.reverse()
#set up variables
sclr = 1
Dec1 = 0
Dec2 = 0
#read through the list and check for a 1, if slot contains 1 then you will add the scalar to the Decimal value
#multiple the scalar by 2
for j in range(len(b1)):
    if b1[j] == "1":
        Dec1 = Dec1 + sclr
    sclr = sclr * 2
    if b1[j] != "1" and b1[j] != "0":#check if the binary number contains anything other than 1 or 0
        print("Not a binary number, cannot continue!")
        exit()#if contains something other than 1 or 0 end the code
#reset the scalar
sclr = 1


for j in range(len(b2)):
    if b2[j] == "1":
        Dec2 = Dec2 + sclr
    sclr = sclr * 2
    if b2[j] != "1" and b2[j] != "0":
        print("Not a binary number, cannot continue!")
        exit()

Dec3 = Dec1 + Dec2#add the two original decimal values into a 3rd value
sclr =1
slot = 0
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
print()
Bin3 = ''#changes list into a string that can be printed out nicely
for x in b3:
    Bin3 += ''+x

print(Bin1, "+", Bin2, "=", Bin3)
