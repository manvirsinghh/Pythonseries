result=2+3
x=5-6
y=50*2
print(result)
print(x)
print(y)

z=x/y
print(z)
m=result//y
print(m)

res=2%3
print(res)

res1=2 **4
print(res1)

res2=abs(-5)
print(res2)

res3=round(3.141,2)
print(res3)


#Floating point number

res=2.5+2.5
print(res)

res1=2.5*5.0
print(res1)

res2=5.0-2.5
print(res2)

#similar other operations like in integer


#complex data type

x=1+2j
y=3+4j
print(x+y)

t=2-4j
s=8-2j
print(t-s)


m=(1+5j) ** 2
print(m)

u=abs(4+5j)
print(u)

q=(3+4j).conjugate()
print(q)


real = (3 + 4j).real  
imag = (3 + 4j).imag

print(real)
print(imag)

#RANDOM NUMBER 
#generating random integer
import random
x=random.randint(1,100)
print(x)


#generate float point number
y=random.uniform(1.0,10.0)
print(y)

import math
n=math.nan
print(n)



x = float('inf')
y = float('-inf')
print(x)  
print(y)