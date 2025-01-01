# Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. 
# The order of elements in a set is undefined though it may consist of various elements.
#create a set
names={'''manvir''','manjot',"manvir",'yuvraj'}
print(names)

# Access Set Items:-
# Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. But you can loop 
# through the set items using a for loop, or ask if a specified value is present in a set, by using the in the keyword.
for i in names:
   print( 'manvir' in names)
 
val={-1,'navneet',(1,2,3)}
print(val)
#we cannot add list as element in set beciase list are mutable and hence not hashable  means their hash values are not constant over time 


# Adding Elements to a Set in Python
# Below are some of the approaches by which we can add elements to a set in Python:

# Using add() Method
# Using update() Method

set3={1,2,3,4,6}
set3.add(5)
print(set3)

myset_1=set()
print("initial set is:")
print(myset_1)
myset_1.add(1)
myset_1.add(2)
myset_1.add((3,4))
print("Set after insertion of elements are:")
print(myset_1) 
for i in range(1, 6):
   myset_1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(myset_1)
 

#  Removing Elements from the Set in Python
# Below are some of the ways by which we can remove elements from the set in Python:

# Using remove() Method or discard() Method
# Using pop() Method
# Using clear() Method
# Using remove() Method or discard() Method
# Elements can be removed from the Sets in Python by using the built-in remove() function but a KeyError arises if the element doesn’t exist in the hashset Python. 
# To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged.




#FROZENSET IN PYTHON
# A frozenset in Python is like a set, but with one important difference: it is immutable.
# Creating a frozenset
fset = frozenset([1, 2, 3, 4])
print(fset)  # Output: frozenset({1, 2, 3, 4})

# You can check its type
print(type(fset))  # Output: <class 'frozenset'>
