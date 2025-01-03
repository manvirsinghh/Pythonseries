num=3
if num%2==0:
    print("no is even")
else:
    print("no is odd")

    #we want to take input from user so we will do in this way
num=int(input("enter the number please:"))
if num%2==0:
        print("no is even")
else:
        print("no is odd")

        #3rd way to check even ,odd
num=int(input("enter the number please;"))
if (num & 1!=0):
            print("no is odd")
else:
            print("no is even")



#program to find sum of n natural  numbers

num=int(input("ENTER THE NUMBER HERE:"))  
print(num*(num+1)/2)
#2nd way to find sum is:

number=int(input("enter the no here:"))
sum=0
for i in range(1,number+1):
  sum=sum+i
print(sum)

# program to display powers of 2 using anonymous functions
# Using lambda to display power of two
power_of_two = lambda x: 2 ** x

# Test the function with a number (e.g., 5)
print(power_of_two(5))  

#progrma to find numbers divisible by other numbers
num1=2
num2=4
if num2 % num1==0:
       print("yes")
else:
       print("no")

#using lambda function
result=lambda num1,num2:"yes" if num2 %num1==0 else "no"
print(result(5,15))

#program to find factors of numbers
def factors(num):
 for i in range(1,num+1):
    if num %i==0:
       print(i)
num=4
factors(num)

#check whether string is palindrome or not
string="manvir"
str=string[::-1]
if string == str:
            print("yes")
else:
            print("no")


#remove punctuations from string
string="Hello!!!, he said ---and went."
punct_string=""
punctuations_marks='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in string:
       if i not in punctuations_marks:
              punct_string=punct_string+i
print(punct_string)

#count no of vowels 
string="manvir"
vowels="aeiouAEIOU"
count=0
for i in string:
       if i in vowels:
              count+=1
print("total vowels are:",count)

#concatenate two lists
list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11,12]
list1.extend(list2)
print(list1)

#program to check is key is already present in dictionary
dict={1:'a',2:'b',3:'c'}
if 1 in dict:
       print("present")

#program to print last element of list
list=[2,5,7,9,10]
print(list[-1])
       
#if we want to access any random element from list
import random
print(random.choice(list))



# print each statement on a new line
print("Python")
print("is easy to learn.")

# new line
print()

# print both the statements on a single line
print("Python", end=" ")
print("is easy to learn.")

#to count occurence of items in list we  use count() method
list=[1,2,3,4,4,6,8,9]
print(list.count(4))

#to remove whitespace from string we use strip method
string=" manvir "
string.strip()
print(string)

#to check whether two strings are anagrams

name1="manvir"
name2="arun"
name1=name1.lower()
name2=name2.lower()

if(len(name1)==len(name2)):
       sorted_name1=sorted(name1)
       sorted_name2=sorted(name2)
       if sorted_name1==sorted_name2:
              print(name1 + "and" +""+name2+"are anagrams")
       else:
              print(name1+"and"+""+name2+"are not angrams")
else:
       print(name1+"and"+""+name2+"are not anagrams")


