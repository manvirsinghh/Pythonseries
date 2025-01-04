a=3
b=5
print(a ^b)

a=5
b=3
print(a ^b)

c=True
d=False
print(c^d)

#xor using operator module which has xor function
import operator
e=5
f=3
print(operator.xor(e,f))

# to checkif string has all character alphabets  we use string.isalpha()

name="manvir"
print(name.isalpha())

name=input("enter the name:")
if name.isalpha():
    print("true")
else:
    print("false")