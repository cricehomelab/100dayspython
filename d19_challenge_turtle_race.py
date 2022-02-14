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


def gamble(screen):
    choice = screen.textinput("who will win?", "Which turtle will win?")
    return choice


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
    winner = 8
    for num, position in enumerate(positions):
        if position == 300:
            no_winner = False
            winner = num
    return no_winner, winner

# Initializing the screen.
screen = Screen()

def run_game(red, orange, yellow, green, blue, purple):
    choice = gamble(screen)
    running = True
    while running:
        check_list = list(check_winner(red.xcor(), orange.xcor(), yellow.xcor(), green.xcor(), blue.xcor(),
                                       purple.xcor()))
        running = check_list[0]
        winner = check_list[1]
        if winner != 8:
            if winner == 0:
                if choice == 'red':
                    print("red wins, YOU WIN!")
                else:
                    print("red wins, you Lose...")
            elif winner == 1:
                if choice == 'orange':
                    print("orange wins, YOU WIN!")
                else:
                    print("orange wins, you Lose...")
            elif winner == 2:
                if choice == 'yellow':
                    print("yellow wins, YOU WIN!")
                else:
                    print("yellow wins, you Lose...")
            elif winner == 3:
                if choice == 'green':
                    print("green wins, YOU WIN!")
                else:
                    print("green wins, you Lose...")
            elif winner == 4:
                if choice == 'blue':
                    print("blue wins, YOU WIN!")
                else:
                    print("blue wins, you Lose...")
            elif winner == 5:
                if choice == 'purple':
                    print("purple wins, YOU WIN!")
                else:
                    print("purple wins, you Lose...")
        pick_turtle()


run_game(red=red, orange=orange, yellow=yellow, green=green, blue=blue, purple=purple)


# Setting screen to exit on click
screen.exitonclick()

