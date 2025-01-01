#if statement

a=45
if a>0:
    print("true")
else:
    print("false")

#if else statement

x=28
if x>0:
    print("x is positive")
else:
    print("x is negative")

number=-2
result="positive" if number>0 else "negative"
print(number)



age=18
experience=50
if age>=18 and experience>25:
    print("eligibletoapply")
else:
    print("noteligibletoapply")

obtainedmarks=int(input("enter the  obtained marks:"))
totalmarks=int(input("enter the total marks:"))
percentage=(obtainedmarks/totalmarks)*100

if(obtainedmarks>80 and  percentage>=85.0):
    print("passed")
else:
    print("failed")

#nested if else statement

x=25
y=56
if x>=10 and y>=90:
    print("true")
else:
    print("false")



marks = int(input("Enter your marks: "))

if marks >= 50:  # First condition: Check if the student has passed
    if marks >= 80:  # Second condition: Excellent if marks >= 80
        print("Excellent")
    elif marks >= 60:  # Condition for "Good"
        print("Good")
    else:  # If marks are between 50 and 59
        print("Average")
else:  # If the student has failed
    print("Failed")

