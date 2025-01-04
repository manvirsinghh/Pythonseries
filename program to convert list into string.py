# Using join() method
# The join() method takes all items in an iterable and joins each element of an iterable (such as list, string, and tuple) into one concatenated string.

# If the iterable contains any non-string values, it raises a TypeError exception.
def listtostring(item):
    string=""
    print(string.join(list))




list=["manvir","manjot","harman"]
print(listtostring(list))


#python string zfill() method  is built in function that is used to add zeroes to beginning of string until specified length is reached and return copy of string
#syntax is : str.zfill(width); here width represent the total length of string after appending the zeroes to the left or beginning of string
#if width given is less than the length of given string then we return string as it is else return new string after adding zeroes
name="manvir"
print(name.zfill(10))
#2nd example
name="harshdeep"
print(name.zfill(5)) # in this case it will return as it is given string because width is less than length of string



# zfill() in case of Sign Prefix
# If the string starts with a prefix like ('+','-'), the zeros are appended after the first sign.

number="+-2972462"
print(number.zfill(10))

number="-7340"
print(number.zfill(6))

#isdecimal() method

# The Python String isdecimal() method is a built-in function that returns true if all the characters in a string are decimal. If one of the characters is not decimal in the string, it returns false.

# In this article, we will learn about the Python String isdecimal() method with the help of examples.

# isdecimal() Syntax
# The Syntax of isdecimal() method is:

# string.isdecimal()
# isdecimal() Parameters
# The isdecimal() method does not take any parameters.

# isdecimal() Return Value
# The isdecimal() method returns

# True if all the characters in a string are valid decimal characters.
# False if one or more characters in a string are not decimal characters.

value="123456"
print(value.isdecimal())


value="97797#899"
print(value.isdecimal())

# usage of == and != operators

email="xyz123@gmail.com"
user_input=input("enter the email please:")
if user_input==email:
    print("email is verfied and correct")
else:
    print("email is not correct")


#2nd example
fruit="mango"
res=input("enter the fruit name here:")
if  fruit==res:
    print("correct")
else:
    print("not correct")


#concatenate strings various methods
#ist method 
# Using join() function to append a string
# Another way to append strings in Python is using the join() method. It has an advantage over the += operator as it can append multiple strings or a list of strings. 
    first_name="Bing"
last_name=" Chandler"

# printing first name
print("The first name is: " + str(first_name))

# printing last name
print("The last name is: " + str(last_name))

# Using join() method to append a string
result= "".join([first_name,last_name])

# print concatenated string
print("The concatenated string is: " + result)


#2nd method use += operator to concatenate the string

first_name="manvir"
last_name="singh"
print(first_name+last_name)

#3rd method is f string
firstname="manvir"
lastname="singh"
print(f"{firstname}{lastname}")

#string swapcase ()method use to change lower case to uppercase and vice versa
name="mango Is tasty"
print(name.swapcase())

#If you want to convert given string into lowercase only it is recommended to use lower() method.
#  Likewise, if you want to convert given string into uppercase only it is recommended to use upper() method.
name="Aviraj"
print(name.lower())

story="once Upon a time"
print(story.upper())


#strip method to remove leading and trailing whitespaces from string  .it has 
# it has also lstrip() and rstrip()


#to count element occurence in list we use count() method
cars = ['Benz','BMW','Ford','Ferrari','volkswagen','BMW']
numbers= [1,5,2,5,7,1,3,3,1,6]
print(numbers.count(5))

import socket
print("the host name of the current system is:",socket.gethostname())

#to check whether if file exist in the system or not we
# check if a file exists using OS Module
# Using the OS module in Python, it’s easy to interact with Operating System. Currently, using OS module methods, we can verify easily if a file or directory exists. 

# os.path.exists()
# os.path.isfile()
# os.path.isdir()
# pathlib.Path.exists()
import os

print(os.path.isfile("C:\\Users\\Win\\Documents"))

#important useful link to learn whole python synatxs and errors and how to solve them
#############################################################################################
# https://wiki.python.org/moin/PythonBooks
#############################################################################################