# #FOR LOOP 
# n=int(input("enter the number:"))
# for i in range(1,n):
#     print(i)

fruit=["mango","apple","guava","strawberry"]
for fruit in fruit:
    print(fruit)

for i in range(10):
    print(i)
 

word="python"
for i in word:
    print(i)
 
for i in range(0,10,2):
    print(i)


string="manvir"
vowel="aeiouAEIOU"
count=0
for i in string:
    if i in vowel:
        count=count+1

        print("Total vowels are:",count)


names=["manvir","majot","harsh"]
for i in names:
    print(i)

marks=(89,68,100)
for mark in marks:
    print(mark)
#print dictionary
d={"manvir":24,"manjot":25}
print(d)
#accessing values in dictionary
print(d["manvir"])

#modifying values in dictionary
d["manvir"]=26
print(d)
#ading new key values pairs
d["harsh"]=21
print(d)

#remove items from dictionary 
del d["manvir"]
print(d)

remove_value=d.pop("manjot")
print(remove_value)
#Dictionary Methods:
# Here are some commonly used dictionary methods:

# keys(): Returns a view of the keys.
# values(): Returns a view of the values.
# items(): Returns a view of the key-value pairs.
# get(key): Returns the value for the given key (returns None if the key doesn't exist).
# clear(): Removes all items from the dictionary.
# copy(): Returns a shallow copy of the dictionary.


#dictionary comprehesnion:-allow dictionary to create in concise way
squared_numbers={ x :x **2  for x in range(0,21)}
print(squared_numbers)

even_numbered={x:x **2 for x in range(0,10) if (x%2==0)}
print(even_numbered)

color="yellow"
for i in color:
    if i=='l':
        continue
    print(i)

