#string data type and its opertions 
#using double quotes
name="manvirsingh"
print(name)
name="manvirsingh \n manjotsingh"
print(name)

#using single quotes
fruit='orange'
print(fruit)

#using triple quotes
fruit='''mango'''
print(fruit)


#Acessing character in string
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
#for access string with negative indexing
print(fruit[-1])
print(fruit[-2])
print(fruit[-3])

#string slicing

name="jasraj"
print(name[0:])
print(name[0:3])
print(name[:])
print(name[:5])
print(name[::-1])

#string is immutable so to manipulate the string we have to  use concatenate ,formatting or slicing methods tocreate  new one based on  originl string
name="manvirsingh"
name='M'+name[1:]
print(name)


s1 = "hello"
s2 = "world"
result = s1 + " " + s2 
print(result)
 ## to delete the entire string we have to use del keyword ,we cannot delete individual charcaters from string  due to immutability
color="red"
del color
 #number data type
