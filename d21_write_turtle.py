# self-experimentation with figuring out how the Turtle.write() method works.

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
number = 3

turtle.write("Hello World" + str(number))
turtle.clear()
turtle.write("Hello World" + str(number + 1))

screen.exitonclick()

