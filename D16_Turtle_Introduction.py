# module that needs to be imported by turtle
# import a module named turtle
#import turtle
# if you just need the Turtle class imported or other modules from the turtle module.
import turtle
from turtle import Turtle, Screen

# creating a turtle object
# 2. Obtained a blueprint of a turtle and assigned it to a variable.
#timmy = turtle.Turtle()
# if you just import Turtle from the turtle module you can do the line below.
timmy = Turtle()
# creating a shape for the turtle the default is an arrow.
timmy.shape("turtle")
# making the timmy object a different color.
timmy.color("green")
# make the turtle move forward by 100 paces
turtle.forward(100)

print(timmy)
# This will output where in memory this object is stored the output from one run is below for me.
# <turtle.Turtle object at 0x011CE658>

# example of object attributes.
my_screen = Screen()
print(my_screen.canvheight) # the height of the turtle window
print(my_screen.canvwidth) # the width of the turtle window

# examples of object methods.
# this method allows the window to be persistent until the exit button is clicked.
my_screen.exitonclick()



