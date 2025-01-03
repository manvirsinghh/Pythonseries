#  String Methods:
# Strings are immutable sequences of characters. They offer a variety of built-in methods to manipulate or query the string
1)len(s): Returns the length of the string. 
len(str)
2)upper(): Converts the string to uppercase.

"hello".upper()  # Output: "HELLO"
3)lower(): Converts the string to lowercase.

"HELLO".lower()  # Output: "hello"
(4)split(separator): Splits the string into a list at the separator.

"apple,orange".split(",")  # Output: ['apple', 'orange']
5)replace(old, new): Replaces a substring with another substring.

"hello world".replace("world", "everyone")  # Output: "hello everyone"
6)find(sub): Returns the index of the first occurrence of sub, or -1 if not found.

"hello world".find("world")  # Output: 6
7) strip(): Removes leading and trailing whitespace.
"  hello  ".strip()  # Output: "hello"
8)join(iterable): Joins elements of an iterable with the string as a separator.

", ".join(["apple", "banana", "cherry"])  # Output: "apple, banana, cherry"
9) startswith(prefix): Checks if the string starts with a specific prefix.

"hello world".startswith("hello")  # Output: True
10)endswith(suffix): Checks if the string ends with a specific suffix.

"hello world".endswith("world")  # Output: True


