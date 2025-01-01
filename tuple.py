# Python Tuple is a collection of objects separated by commas. A tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main
# difference between both is Python tuple is immutable, unlike the Python list which is mutable.

name=("manivr","manjot")
print(name)
print(type(name))
#Accessing Values in Python Tuples
t=(10,20,30)
print(t[0])
print(t[-3])
 # traversing a tuple
for i in t:
    print(i)
    #concatenating a tuple
    t1=(-30,-59,-103)
    t2=(20,5,78)
    print(t1+t2)
#nesting tuples ie tuple inside tuple
t3=(t1,t2)
print(t3)

#repitition tuples
t4=("manvir",) *3
print(t4)
 #slicing tuple
 # code to test slicing
t = (0 ,1, 2, 3)

print(t[1:])
print(t[::-1])
print(t[2:4])

#deleting a tuple
del t

 #length of tuple
movies=('''nikka zaildar''','''rbb da radio''','''bumbukat''')
print(len(movies))

#Tuples in Python are heterogeneous in nature. This means tuples support elements with multiple datatypes
tuple=("manvir",'python',25,100,0.5,-5.6,['apple','mango'],{'name':'manjot','class':'MBA'})
print(tuple)


# Converting a List to a Tuple
# We can convert a list in Python to a tuple by using the tuple() constructor and passing the list as its parameters.
# Code for converting a list and a string into a tuple
# Rename any variable called 'tuple' to something else


#we can create a tuple without round bracket
t=4,5,6,7,8,9
print(t)

t=()
print(t)

#create tuple using tuple packing
a,b,c=5,6,7
t=(a,b,c)
print(t)
