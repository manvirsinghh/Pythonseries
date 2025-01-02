# The Array can be created in Python by importing the array module to the python program.
from array import *
# a=array(typecode,[initializers])

#how to access array element
# Typecode: 'i' indicates that the array will store integers.

a=array('i',[2,3,4,5,6])
print("first element is:",a[0])
print("second element is:",a[1])
print("last element is :",a[-1])

#for storing floating point numbers we have to add f instead of i


#To store different types of data types elements we will
#  prefer to use list instead of array because array holds homogeneous data types elements
#delete the array element

number=array('i',[2,3,4,5,6,6,7])
del number[2]
print(number)
print(len(number)) 