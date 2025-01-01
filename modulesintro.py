#Modules in pythons are files that contain built -in functions and in this we will see how to import python modules and how can we create python modules
#1) calc module

from math import sqrt,factorial
#or from math import *

print(sqrt(16))
print(factorial(5))


from math import sin
print(sin(90))

help('modules')

#Using dir() to Explore Modules
# Once you have imported a module, you can use the dir() function to view its contents (functions, classes, variables, etc.).
import math
print(dir(math))


#we can rename the module name 
import math as mt
print(mt.sqrt(25))
print(mt.factorial(2))