# ASCII: ASCII is an acronym that stands for American Standard Code for Information Interchange. A specific numerical value is given to different characters and symbols for computers to store and manipulate in ASCII.


# It is case sensitive. The same character, having different formats (upper case and lower case), has a different value. For example, The ASCII value of "A" is 65 while the ASCII value of "a" is 97.

#we will use ord() function to convert character to integer value ie ascii value

char=input("enter the char:")
print("the ascii value of num is:",ord(char))



print("enter the string: \n ")
string=input()
for k in string:
    print(ord(k))




string=input("enter the string:")
for i in string:
    print(ord(i))
   


   #Python Function to Display Calendar
import calendar

year=int(input("enter the year:"))
month=int(input("enter the month:"))

print(calendar.month(year,month))

