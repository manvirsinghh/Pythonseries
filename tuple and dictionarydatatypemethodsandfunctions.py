Tuple (tuple) Methods:
Tuples are immutable sequences. You cannot modify them directly, but they offer useful methods to query them.

len(tuple): Returns the length of the tuple
len((1, 2, 3))  # Output: 3


count(item): Returns the number of occurrences of an item in the tuple.
tup = (1, 2, 3, 2)
tup.count(2)  # Output: 2

index(item): Returns the index of the first occurrence of an item
tup = (1, 2, 3)
tup.index(2)  # Output: 1

Slicing: Extract a portion of the tuple
tup = (1, 2, 3, 4, 5)
tup[1:3]  # Output: (2, 3)



Dictionary (dict) Methods:
Dictionaries are unordered collections of key-value pairs.


len(dict): Returns the number of items (key-value pairs) in the dictionary
len({"name": "Alice", "age": 25})  # Output: 2

get(key): Returns the value associated with a key.

my_dict = {"name": "Alice", "age": 25}
my_dict.get("name")  # Output: "Alice"


keys(): Returns a view object displaying all the keys in the dictionary.
my_dict.keys()  # Output: dict_keys(['name', 'age'])


values(): Returns a view object displaying all the values in the dictionary
my_dict.values()  # Output: dict_values(['Alice', 25])

items(): Returns a view object displaying all key-value pairs.
my_dict.items()  # Output: dict_items([('name', 'Alice'), ('age', 25)])

update(dict2): Merges another dictionary into the current one
my_dict.update({"city": "New York"})  # Updates my_dict

pop(key): Removes the key-value pair and returns the value.
my_dict.pop("age")  # Output: 25, my_dict becomes {'name': 'Alice'}




