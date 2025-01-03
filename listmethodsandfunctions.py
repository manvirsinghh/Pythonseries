
Here is a comprehensive list of commonly used methods and functions for each Python data type, along with examples on how they can be used in programming problems. You can use these methods in your programs to manipulate and solve problems related to various data types.

1. String (str) Methods:
Strings are immutable sequences of characters. They offer a variety of built-in methods to manipulate or query the string.

Methods and Functions:
len(s): Returns the length of the string.
python
Copy code
len("hello")  # Output: 5
upper(): Converts the string to uppercase.
python
Copy code
"hello".upper()  # Output: "HELLO"
lower(): Converts the string to lowercase.
python
Copy code
"HELLO".lower()  # Output: "hello"
split(separator): Splits the string into a list at the separator.
python
Copy code
"apple,orange".split(",")  # Output: ['apple', 'orange']
replace(old, new): Replaces a substring with another substring.
python
Copy code
"hello world".replace("world", "everyone")  # Output: "hello everyone"
find(sub): Returns the index of the first occurrence of sub, or -1 if not found.
python
Copy code
"hello world".find("world")  # Output: 6
strip(): Removes leading and trailing whitespace.
python
Copy code
"  hello  ".strip()  # Output: "hello"
join(iterable): Joins elements of an iterable with the string as a separator.
python
Copy code
", ".join(["apple", "banana", "cherry"])  # Output: "apple, banana, cherry"
startswith(prefix): Checks if the string starts with a specific prefix.
python
Copy code
"hello world".startswith("hello")  # Output: True
endswith(suffix): Checks if the string ends with a specific suffix.
python
Copy code
"hello world".endswith("world")  # Output: True
2. List (list) Methods:
Lists are ordered, mutable collections. You can use a variety of methods to add, remove, or access elements.

Methods and Functions:
len(list): Returns the length of the list.

len([1, 2, 3])  # Output: 3
append(item): Adds an item to the end of the list.

lst = [1, 2, 3]
lst.append(4)  # lst becomes [1, 2, 3, 4]
insert(index, item): Inserts an item at a specified index.
lst = [1, 2, 3]
lst.insert(1, 4)  # lst becomes [1, 4, 2, 3]
remove(item): Removes the first occurrence of the specified item.

lst = [1, 2, 3, 2]
lst.remove(2)  # lst becomes [1, 3, 2]
pop(index): Removes and returns the item at a specified index.

lst = [1, 2, 3]
lst.pop(1)  # Output: 2, lst becomes [1, 3]
sort(): Sorts the list in place.

lst = [3, 1, 2]
lst.sort()  # lst becomes [1, 2, 3]
reverse(): Reverses the order of the list.

lst = [1, 2, 3]
lst.reverse()  # lst becomes [3, 2, 1]
extend(iterable): Adds all items from another iterable to the list.
lst = [1, 2]
lst.extend([3, 4])  # lst becomes [1, 2, 3, 4]
index(item): Returns the index of the first occurrence of the item.

lst = [1, 2, 3]
lst.index(2)  # Output: 1
count(item): Returns the number of occurrences of the item.
lst = [1, 2, 2, 3]
lst.count(2)  # Output: 2