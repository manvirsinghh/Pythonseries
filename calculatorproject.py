print("Welcome to the calculator")

print("Select the Operation:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")

# Taking input values
num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))
operation = input("Enter the number for operation (1/2/3/4/5/6)")

# Performing calculations based on the chosen operation
if operation == '1':
    result = num1 + num2
    print("The result is:", result)
elif operation == '2':
    result = num1 - num2
    print("The result is:", result)
elif operation == '3':
    result = num1 * num2
    print("The result is:", result)
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '5':
    result=num1%num2
    print("the result is :",result)
else:
    print("invalid choice,plz enter the valid choice")
