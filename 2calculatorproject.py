#2 CALCULATOR PROJECT
import math


# Function to add two numbers
def add_numbers():
   
    num1 = int(input("enter the first number:"))
  
    num2 = int(input("enter the second number:"))
    result = num1 + num2
    print(result)

# Function to subtract two numbers
def sub_numbers():
  
    num1 = int(input("enter the first number:"))
   
    num2 = int(input("enter the second number:"))
    if num1 < num2:
        print(abs(num1 - num2))  # Absolute difference if num1 < num2
    else:
        print(num1 - num2)

# Function to multiply two numbers
def multiply_numbers():
   
    num1 = int(input("enter the first number:"))
  
    num2 = int(input("enter the second number:"))
    if num1 == 0 or num2 == 0:
        print("multiplication is 0")
    else:
        print(num1 * num2)

# Function to divide two numbers
def division_numbers():
  
    num1 = int(input("enter the first number:"))
   
    num2 = int(input("enter the second number:"))
    if num2 == 0:
        print("division is not possible, please enter a non-zero number:")
    else:
        print(num1 / num2)

# Function to calculate the square root of a number
def sqrt_root():
 
    num = int(input("enter the no here:"))
    print(math.sqrt(num))

# Function to calculate the power of a number
def power():
 
    num1 = int(input("enter the first no here:"))

    num2 = int(input("enter the second number"))
    if num2 == 0:
        print(1)
    else:
        print(math.pow(num1, num2))

# Main program loop
print("welcome to my calculator:")
while True:
    print("1. 'Addition'")
    print("2. 'Subtraction'")
    print("3. 'Multiplication'")
    print("4. 'Division'")
    print("5. 'Square Root'")
    print("6. 'Power'")
    print("7. 'Exit'")

    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        add_numbers()
    elif choice == 2:
        sub_numbers()
    elif choice == 3:
        multiply_numbers()
    elif choice == 4:
        division_numbers()
    elif choice == 5:
        sqrt_root()
    elif choice == 6:
        power()
    elif choice == 7:
        print("exit")
        break
    else:
        print("enter the valid choice please!")
  