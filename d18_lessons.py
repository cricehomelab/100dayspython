# import turtle
# aliases the turtle module as an alias ("t" in this case).
import turtle as t
# this imports everything but can be confusing as code grows best to avoid this.
import turtle

# from turtle import *

tim = t.Turtle()
tim.shape("turtle")
tim.color("lime green")
# timmy_the_turtle.forward(100)
# challenge 1: draw a square
# timmy_the_turtle.setheading(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.setheading(180)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.setheading(270)
# timmy_the_turtle.forward(100)
# The best solution for this.
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Challenge 2: draw a dashed line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Challenge 3 drawing shapes in sequence.
# import random
# turtle_colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
#                  "cyan", "turquoise", "lime", "green", "darkgreen", "chocolate", "brown", "black", "gray", "pink"]
#
# for shapes in range(3, 11):
#     tim.color(random.choice(turtle_colors))
#     turn_angle = 360 / shapes
#     i = 0
#     for i in range(shapes):
#         tim.forward(100)
#         tim.right(turn_angle)

# Challenge 4 draw a random walk.
# I added a second turtle object for fun.
# import random
# tom = Turtle()
# directions = [0, 90, 180, 270]
# turtle_colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
#                   "cyan", "turquoise", "lime", "green", "darkgreen", "chocolate", "brown", "gray", "pink"]
# tim.pensize(10)
# tom.pensize(5)
# tim.speed(0)
# tom.speed(0)
# for _ in range(200):
#     tom.color("black")
#     tim.color(random.choice(turtle_colors))
#     tom.color(random.choice(turtle_colors))
#     tim.forward(20)
#     tom.forward(20)
#     tim.left(random.choice(directions))
#     tom.left(random.choice(directions))

# # setting truly random colors for the pen.
import random

#
# # setting the colormode to rgb instead of defined color names.
t.colormode(255)


#
# directions = [0, 90, 180, 270]
#
# # this has been removed.
# #turtle_colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
# #                  "cyan", "turquoise", "lime", "green", "darkgreen", "chocolate", "brown", "gray", "pink"]
#
# tim.pensize(10)
#
# tim.speed(0)
#
#
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#
#
# for _ in range(200):
#      tim.pencolor(color())
#      tim.forward(20)
#      tim.left(random.choice(directions))

# Challenge 5: make a spirograph
# Draw a circle with radius 100
# repeatedly draw a circle and change the tilt slightly each time.

# draw a circle
tim.speed(0)
tim.shape("arrow")
# this works but does not stop when it gets "all the way around"
# for _ in range(100):
#     tim.circle(100)
#     tim.left(5)
#     tim.color(color())

# this comes full circle.
def draw_spirograph(size_of_gap):
    for _ in range(round(360 / size_of_gap)):
        tim.color(color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

# aside setting up a way to move the turtle from WASD commands
# def up():
#     timmy_the_turtle.setheading(90)
#     timmy_the_turtle.forward(10)
#
#
# def down():
#     timmy_the_turtle.setheading(270)
#     timmy_the_turtle.forward(10)
#
#
# def left():
#     timmy_the_turtle.setheading(180)
#     timmy_the_turtle.forward(10)
#
#
# def right():
#     timmy_the_turtle.setheading(0)
#     timmy_the_turtle.forward(10)
#
#
# listen()
# onkey(up, 'w')
# onkey(down, 's')
# onkey(left, 'a')
# onkey(right, 'd')
