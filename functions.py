# #Common Built-in Functions in Python:
# print() – Prints output to the console.
# len() – Returns the length of an object.
# max() – Returns the largest item in an iterable.
# min() – Returns the smallest item in an iterable.
# sum() – Sums all items in an iterable.
# sorted() – Returns a sorted list of elements.
# type() – Returns the type of an object.
# input() – Takes input from the user.
# abs() – Returns the absolute value of a number.
# range() – Generates a sequence of numbers.

#defining a function
# def function_name(argumwnts):
#     # function body
#     return value

#add two numbers using function
# a=int(input("enter the valueof a:"))
# b=int(input("enter the value of b:"))
# def sum(a,b):
#     return a+b
# # result=sum(a,b)
# # print(result)
# print("sum  a and b is:",sum(a,b))

#function types:
#1)Function without parameter and return type
def name():
    print("manvir")
name()

#function with parameter
def multiply(a,b):
    print(a*b)


result=multiply(5,7)

#function with return type

def sum(a,b):
    print("sum of a and b are:",sum(a,b))

    #lambda or anonymous functions
    #syntax:-lambda arguments:expression
    #example1

add=lambda a,b,c:a+b+c
print(add(2,3,4))

#example 2
value=lambda x:"even" if x%2==0 else "odd"
print(value(2))
print(value(3))

#example 3
number=lambda x,y:x if x>y else y
print(number(2,3))

#similarly we check even ,odd,negativ ,psotive conditions using lambda function
#the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
