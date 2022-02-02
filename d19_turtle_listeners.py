# I went way off lesson here to make the turtle move like an isometric RPG because I love the top down RPGs. 

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("circle")

screen.listen()

tim.penup()

def up():
    tim.sety( tim.pos()[1] + 25)


def right():
    tim.setx( tim.pos()[0] + 25)


def down():
    tim.sety( tim.pos()[1] - 25)


def left():
    tim.setx( tim.pos()[0] - 25)


screen.onkeypress(fun=up, key="w")
screen.onkeypress(fun=left, key="a")
screen.onkeypress(fun=down, key="s")
screen.onkeypress(fun=right, key="d")





screen.exitonclick()