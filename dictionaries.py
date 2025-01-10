# A dictionary in Python is an unordered collection of data values, used to store data values like a map,
#  unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair.
# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)


# Accessing Key-value in Dictionary
# In order to access the items of a dictionary refer to its key name. 
# Key can be used inside square brackets. Using get() method we can access the dictionary elements.

dictionary={'marks':78,'age':45}
print(dictionary)
print(dictionary['marks'])
print(dictionary.get('marks'))
print(d1.items())
print(d1.pop)
print(d1.keys())
print(d1.values())
print(d1.items())