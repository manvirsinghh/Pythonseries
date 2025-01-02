#syntax to create a class:
# class class_name:

#ist example
class MyClass:
    x = 5

# Creating an instance of MyClass outside the class definition
p1 = MyClass()

# Printing the value of 'x' from the instance 'p1'
print(p1.x)

#second example
class name:
    x="manvir"
p1=name()
print(p1.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        p1=person("manvir",23)
        print(p1.name)
        print(p1.age)