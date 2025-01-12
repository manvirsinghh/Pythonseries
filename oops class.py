
# 1)CLASS:

# In Python, a class is a blueprint or template for creating objects. 
# It encapsulates data (attributes) and functions (methods) that define the characteristics and behaviors of objects belonging to that class.



# Objects: Instances of a class. Each object has its own unique set of attribute values.
# Attributes: Variables that represent the properties of an object. They can be:
# Instance Attributes: Unique to each object.
# Class Attributes: Shared by all objects of the class.
# Methods: Functions defined within a class. They operate on the object's data and define its behavior.

#creating a class

class Myclass:
    #class attribute
    class_variable="this is class attribute"
    def __init__ (self,attribute1,attribute2):
    #instance attributes
      self.attribute1=attribute1
      self.attribute2=attribute2
    def method(self):
    #method definition
      print("this is method of Myclass")

#class MyClass: defines a class named MyClass.
# class_variable: A class attribute shared by all instances of MyClass.
# __init__ (constructor): A special method that initializes instance attributes when an object is created.
# self: Refers to the current object instance.
# method1: A method that performs an action.

#Creating objects:
object1 = Myclass("value1", "value2")
object2 = Myclass("value3", "value4")