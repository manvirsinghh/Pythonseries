# #In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list
# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List are ordered. It maintain the order of elements based on how they are added.
# Accessing items in List can be done directly using their position (index), starting from 0.

a=[10,20,30,40,50,60]
print(a)
print(a[0]) #to access partiular index list element
print(a[1])
print(a[2])
print(len(a)) #to find length of list
a.append(70) #to append new item in list 
print(a)
a.remove(70)
print(a)
#create a list using list constructor

a=list((1,2,5.6,"apple",'mango'))# include tuple into list
print(a)
b=list([4,2.5,{'age':20,'marks':90}]) #include dictionary into list
print(b)

#creating a list with repeated elements
list1=[3]*3
print(list1)
list2=[0] *7
print(list2)

#Accessing the list elements
marks=[86,90,95,75,78]
print(marks[0]) # to access any index value of list
print(marks[len(marks)-1]) #to access last element of list using this method 
print(marks[-1]) # second way to access last element of list using this method
#adding elements to list
marks.append(60)
marks.insert(6,55)
marks.extend([100,89,60])
print(marks)

#update the elements of list
marks[0]=68
print(marks)
#We can remove elements from a list using:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

print(marks.remove(68))
print(marks.pop(1))
del marks[2]
print(marks)

#iterating over list(ist method)

colors=["red","orange","pink","yellow","purple","black","skyblue"]
for  color in colors:
    print(color)

# We can use the range() method with for loop to traverse the list. (2 method)
a=len(colors)
for i in range(a):
    print(colors[i])
#3rd method Using enumerate()
# We can also use the enumerate() function to iterate through the list. 
# This method provides both the index (i) and the value (val) of each element during the loop.
for i ,val in enumerate(colors):
    print(i,val)

#nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2][2])

#sort a list
a=[-10,5,2,9,1,35]
a.sort()
print(a)
