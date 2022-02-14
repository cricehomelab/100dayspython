from turtle import Turtle, Screen
import random

# initializing the turtles, putting pen up, setting appropriate color, setting shape, and placing them at starting
# positions.
red = Turtle()
red.penup()
red.shape("turtle")
red.color("red")
red.setposition(-450, 60)

orange = Turtle()
orange.penup()
orange.shape("turtle")
orange.color("orange")
orange.setposition(-450, 30)

yellow = Turtle()
yellow.penup()
yellow.shape("turtle")
yellow.color("yellow")
yellow.setposition(-450, 0)

green = Turtle()
green.penup()
green.shape("turtle")
green.color("green")
green.setposition(-450, -30)

blue = Turtle()
blue.penup()
blue.shape("turtle")
blue.color("blue")
blue.setposition(-450, -60)

purple = Turtle()
purple.penup()
purple.shape("turtle")
purple.color("purple")
purple.setposition(-450, -90)

black = Turtle()
black.shape("turtle")
black.color("black")
black.penup()
black.setposition(300, -120)
black.pendown()
black.left(90)
black.forward(210)


def pick_turtle():
    number = random.randint(0, 5)
    if number == 0:
        red.forward(10)
    elif number == 1:
        orange.forward(10)
    elif number == 2:
        yellow.forward(10)
    elif number == 3:
        green.forward(10)
    elif number == 4:
        blue.forward(10)
    elif number == 5:
        purple.forward(10)


def check_winner(red, orange, yellow, green, blue, purple):
    positions = [red, orange, yellow, green, blue, purple]
    no_winner = True
    for position in positions:
        if position == 300:
            no_winner = False
    return no_winner


def run_game(red, orange, yellow, green, blue, purple):
    running = True
    while running:
        running = check_winner(red.xcor(), orange.xcor(), yellow.xcor(), green.xcor(), blue.xcor(), purple.xcor())
        pick_turtle()


run_game(red=red, orange=orange, yellow=yellow, green=green, blue=blue, purple=purple)

# Initializing the screen.
screen = Screen()
# Setting screen to exit on click
screen.exitonclick()

