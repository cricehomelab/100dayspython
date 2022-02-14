from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# move_forwards is a function as an input.
# this is an example of a higher order function. The onkey() function takes another function to do something.
screen.onkey(key="space", fun=move_forwards)
# exitonclick() allows for the window to not close until the window is clicked on.
screen.exitonclick()
