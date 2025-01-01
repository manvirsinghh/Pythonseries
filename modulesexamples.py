#Python Built-in modules
# There are several built-in modules in Python, which you can import whenever you like.
import math 
print(math.sqrt(2))
print(math.factorial(6))
print(math.pi)
print(math.degrees(2))
print(math.radians(2))
print(math.sin(2))


import random
print(random.randint(0,4))
print(random.random())
print(random.random() *100)

List=["manvir","singh","manjot","singh"]
# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List))

#datetime module
# The datetime.now() method returns the current date and time.
import datetime
now=datetime.datetime.now()
print(now)
#use to find current date
currentdate=datetime.date.today()
print(currentdate)

from emoji import emojize 
print(emojize(":thumbs_up:"))
#emojize(":thumbs_up:"):
# The emoji module is not part of Python's standard library, meaning it is not included by default when you install Python. 
#ou need to install it separately.
# The emojize function is provided by the emoji library.
# It converts the text ":thumbs_up:" (which is the emoji code) into the actual thumbs-up emoji (👍).

from emoji import emojize
print(emojize(":thumbs_down:"))

print(emojize(":rocket:"))
