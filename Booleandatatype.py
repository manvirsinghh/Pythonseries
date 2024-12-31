a=True
print(a)
print(type(a))

b=False
print(b)
print(type(b))

x=None 
print(bool(x))

x=()
print(x)
print(bool(x))

#BOOLEAN OPERATORS

# or,and,not ==,!=
a=2
b=4
c=6
if a>b and b>c:
 print(a)
else:
 print(b)


 m=5
 n=6
 o=7
 if m and n and o:
  print("true")
 else:
  print("false")

  a=0
  if not a:
   print("False")


a=1
b=0

if a==0:
    print("false")
else:
    print("true")

    #is keyword is used to test whether two variables belong to the same object. 
    # The test will return True if the two objects are the same 
    # else it will return False even if the two objects are 100% equal.

    x=10
    y=10
    if x is y:
      print("true")
    else:
      print("false")



#in operator checks for the membership i.e. checks if the value is present in a list, tuple, range, string, etc.
a=[1,2,3,4,5,6,7,8,9,10]
if 12 in a:
  print("false")
