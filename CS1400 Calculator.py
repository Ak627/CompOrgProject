#___________________________________________________________________
# Six function calculator using Python
# Author: Sam Eneglbert CS1400 Team 5 (Alex, Sam, Dawson, and Brian)
#___________________________________________________________________
# user input section
name = input("What is your name? ") # asks for user's name  
print(f"Hello there {name}!") # prints hello message to user 
def prompt_menu(): # menu generation and first and second operators 
    a = float (input("Enter first number ")) 
    b = float(input("Enter second number "))
    print ("""
Choose an operation from the list 
           1. Addition
           2. Subtraction
           3. Mulipication 
           4. Exponent 
           5. Division
           6. Division with a remainder 
           """) # menu selection 
    op = int(input("Enter a selection number "))
    return  a, b, op 
def calculate():
    a, b, op = prompt_menu()
    if op == 1: 
        print("Sum {} + {} = {}".format(a,b,a+b)) # Addition function 
    elif op == 2: 
        print("Difference {} - {} = {}".format(a,b,a-b)) # Subtraction function
    elif op == 3: 
        print("Product {} * {} = {}".format(a,b,a*b)) # Multipication function
    elif op == 4: 
        print("Power {} ^ {} = {}".format(a,b,a**b)) # Exponent function 
    elif op == 5:
        try: 
            print("Quotient {} / {} = {}".format(a,b,a/b)) # Division function  
        except: 
            print("Division by 0 isn't possible")
    elif op == 6:
        try: 
            print("Division remainder: {} / {} = {} Remainder:{}".format(a,b,a//b,a%b)) # Division with a remainder function 
        except: 
            print("Division by 0 isn't possible")
    else:
            print("No other choice")
    loop() 

def loop(): # continue or end prompt 
    choice = input("Do you want to continue? (Yes/No]): ")
    if choice.upper() == "Yes": 
        calculate() 
    elif choice.upper() == "No": 
        print("Goodbye!")
loop() 

calculate() # calculate will initiate the loop of (Yes/No):    





 

