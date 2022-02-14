# Goal: build etch a sketch program with turtle.
# Inputs:
# W = forwards
# S = backwards
# A = rotate counter-clockwise
# D = rotate clockwise
# C = clear drawing re-center the arrow.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Movement functions
def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def rotate_right():
    tim.right(10)


def rotate_left():
    tim.left(10)


def clear_screen():
    tim.reset()


screen.listen()

# Key presses that perform the functions actions.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="c", fun=clear_screen)

# allows screen to exit when the turtle window is clicked on. 
screen.exitonclick()
