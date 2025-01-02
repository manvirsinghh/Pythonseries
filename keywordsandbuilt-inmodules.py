import keyword
print("the list of keywords are:")
print(keyword.kwlist)

#Built in python modules
#Math module
import math
square=math.sqrt(25)
print(square)
print(math.factorial(5))
print(math.pow(2,3))
print(math.gcd(2,4))
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(-math.inf)

#calculate the circumference of circle using pi function
radius=int(input("Enter the value of r:"))
print(math.pi *(2*radius))

import math
x=6.385
print(math.ceil(x))
print(math.floor(x))

x=-5
print(math.fabs(x))
print(math.exp(x))

angle=math.pi/4
print(math.sin(angle))

#random module

#generate random integer 
import random
result=random.randint(1,10)
print(result)

#random floating point number bewteen 0.0 and 1.0
result1=random.random()
print(result1)

#shuffle() function to shuffle list randomly
list=[1,2,3,4,5]
random.shuffle(list)
print(list)

#choice function to select random element 
random_s=random.choice("manvir")
print(random_s)