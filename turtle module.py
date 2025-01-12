# turtle module is used to draw or made various shapes .
# following are the methods or functions that turtle module has are as follows
# Method	   Parameter	    Description
# Turtle()	None	    Creates and returns a new turtle object
# forward()	amount	    Moves the turtle forward by the specified amount
# backward()	amount	    Moves the turtle backward by the specified amount
# right()	    angle	    Turns the turtle clockwise
# left()	    angle	    Turns the turtle counterclockwise
# penup()	    None	    Picks up the turtle’s Pen
# pendown()	None	    Puts down the turtle’s Pen
# up()	    None	    Picks up the turtle’s Pen
# down()	    None	    Puts down the turtle’s Pen
# color()	   Color name	Changes the color of the turtle’s pen
# fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon
# heading()	None	    Returns the current heading
# position()	None	    Returns the current position
# goto()	    x, y	    Move the turtle to position x,y
# begin_fill()None	    Remember the starting point for a filled polygon
# end_fill()	None	   Close the polygon and fill with the current fill color
# dot()	    None	   Leave the dot at the current position
# stamp()	    None	   Leaves an impression of a turtle shape at the current location
# shape()	  shapename	   Should be ‘arrow’, ‘classic’, ‘turtle’ or 







# The steps for executing a turtle program follows 4 steps:  

# 1)Import the turtle module
# 2)Create a turtle to control.
# 3)Draw around using the turtle methods.
# 4)Run turtle.done().




# So as stated above, before we can use turtle, we need to import it. We import it as : 

# from turtle import *
# # or
# import turtle
# After importing the turtle library and making all the turtle functionalities available to us, we need to create a new drawing board(window) and a turtle. Let’s call the window as wn and the turtle as skk. So we code as: 

# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# Now that we have created the window and the turtle, we need to move the turtle. To move forward 100 pixels in the direction skk is facing, we code: 

# skk.forward(100)
# We have moved skk 100 pixels forward, Awesome! Now we complete the program with the done() function and We’re done! 

# turtle.done()
# So, we have created a program that draws a line 100 pixels long. We can draw various shapes and fill different colors using turtle methods. 
# There’s plethora of functions and programs to be coded using the turtle library in python. Let’s learn to draw some of the basic shapes. 

#1 square using turtle module

import turtle
# window=turtle.Screen()
# window.bgcolor("light blue")
# window.title("Turtle")
# skk=turtle.Turtle()
# for i in range(4):
#  skk.forward(50)
#  skk.right(90)
# turtle.done()


# Python program to draw star 
# using Turtle Programming 
import turtle 
star = turtle.Turtle() 

star.right(75) 
star.forward(100) 

for i in range(4): 
	star.right(144) 
	star.forward(100) 
	
turtle.done() 
