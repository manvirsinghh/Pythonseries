# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# Before Python 3.6 we had to use the format() method.

# F-Strings
# F-string allows you to format selected parts of a string.

# To specify a string as an f-string, simply put an f in front of the string literal, like this:

name=f"manvir"
print(name)

# To format values in an f-string, add placeholders {}, 
# a placeholder can contain variables, operations, functions, and modifiers to format the value.

age=58
txt=f"the rohan is  {age} years old"
print(txt)

# A placeholder can also include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:

age=58
txt=f"the rohan is  {age:.2f} years old"
print(txt)


#cmath module is improtant for complex numbers