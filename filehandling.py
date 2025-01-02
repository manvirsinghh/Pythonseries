# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.

# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)
#SYNTAX 
f=open("set.py")

#read lines
#first case to read  one line using readline() method
f=open("set.py")
print(f.readline())

#second case to read two lines using readline() method
f=open("set.py")
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:

for i in f:
    print(i)

    #close a file
f=open("list.py")
print(f.readline())
f.close()






# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f=open("set.py")
print(f.read(5))


#to write into into first open the file and then write in it using write function
#TO DELETE THE FILE WE MUST HAVE TO IMPORT OS MODULE AND IMPORT os.remove() function
import os
os.remove("abc.txt")

import os
if os.path.exists("abc.txt"):
  os.remove("abc.txt")
else:
  print("The file does not exist")