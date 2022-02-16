# Part 1:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake using buttons.
# Part 2:
# 4. Detect Collision with food.
# 5. Keep track of the score.
# 6. game over scenarios
#   A. Collision with wall.
#   B. Collision with snake body.
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Let's Play a game of Snake.")
screen.tracer(0)

# My solution for creating the start of the turtle (works)
# This is a mini challenge to determine how the snake should be generated.
# scratch work to determine what my for loop should do.
# turtle1 = Turtle()
# turtle1.shape("square")
# turtle1.color("white")
# turtle1.penup()
# turtle1.goto(0, 0)
# turtle2 = Turtle()
# turtle2.shape("square")
# turtle2.color("white")
# turtle2.penup()
# turtle2.goto(-20, 0)

# for turtles in range(3):
#     snake = Turtle()
#     snake.shape("square")
#     snake.color("white")
#     snake.penup()
#     # print(f'{turtles} position is {turtles * -20}, 0')
#     snake.goto((turtles * -20), 0)

# instructor solution
starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
#   Range function written in C, so you can't use keywords with it. We are using positional arguements but this is the
#   What arguments we are specifying. ++
#                  range(start, stop, step)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()
