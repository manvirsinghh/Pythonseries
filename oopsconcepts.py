# #class 
# class ClassName:
#     #statements Pascal case
#     class Instructor:
#        #create an object 
#         instructor_1=Instructor()

class Instructor:
     def __init__(self):
        print("creating a new object")
Instructor_1=Instructor()
print(type(Instructor_1))
Instructor_1.name="manvir"
print(Instructor_1.name)

class CarDesign:
     pass #for time being i have not do here anything else that why i use here pass statement
car1=CarDesign()
# print(type(car1))
car1.name="ritz"
car1.model="2019"
print(car1.name)
print(car1.model)

car2=CarDesign()
car2.name="maruti"
car2.model="2018"
print(car2.name)
print(car2.model)

#in c++ we have constructor to initilaize the objects but in python we have __init__ method to initialize the objects 
#everytime we create the object of class ,the __init__function will be called and it is used to initialize the attributes of the particular object
#and when created object at that point the self become that object for time being and continue in simliar way
#1 example
class Instructor:
    def __init__(self,instructor_name,address):
     self.name=instructor_name
     self.addresss=address

instructor_1=Instructor("manvir","ludhiana")
print(instructor_1.name)
instructor_2=Instructor("manjot","jalandhar")
print(instructor_2.name)
#in this example we have understood the usage of init method and self keyword and how its is called when object is created and help 
# in initialize the objects of particular class
#class method
class Instructor:
    def __init__(self,name,address):
        self.name =name
        self.address =address
    def display(self):
Instructor_1=Instructor("manvir","gurgaon")
print(instructor_1.name)
