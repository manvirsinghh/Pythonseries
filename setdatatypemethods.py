 Set (set) Methods:
Sets are unordered collections of unique elements. They support mathematical set operations.

Methods and Functions:
len(set): Returns the number of elements in the set.

len({1, 2, 3})  # Output: 3
add(item): Adds an item to the set.

my_set = {1, 2, 3}
my_set.add(4)  # my_set becomes {1, 2, 3, 4}
remove(item): Removes an item from the set (raises an error if not found).

my_set = {1, 2, 3}
my_set.remove(2)  # my_set becomes {1, 3}
discard(item): Removes an item if it exists in the set (does not raise an error if not found).

my_set.discard(4)  # my_set remains {1, 2, 3}
union(set2): Returns a new set with elements from both sets.

set1 = {1, 2}
set2 = {2, 3}
set1.union(set2)  # Output: {1, 2, 3}
intersection(set2): Returns the intersection of two sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection(set2)  # Output: {2, 3}
difference(set2): Returns the elements in set1 that are not in set2.

set1.difference(set2)  # Output: {1}
pop(): Removes and returns an arbitrary element from the set.


my_set = {1, 2, 3}
my_set.pop()  # Removes and returns an element