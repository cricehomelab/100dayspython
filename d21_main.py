import d21_snake
import d21_food
from d21_scoreboard import Scoreboard
# import d21_scoreboard
import time
from turtle import Screen

BOUNDARY_POSITIVE = 299
BOUNDARY_NEGATIVE = -299

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Let's Play a game of Snake.")
screen.tracer(0)

snake = d21_snake.Snake()
food = d21_food.Food()
scoreboard = Scoreboard()

# keep track of score
score = 0
# From my solution to implement d21_scoreboard.py functionality.
# display = d21_scoreboard.Scoreboard()
# display.scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # From my solution to implement d21_scoreboard.py functionality.
        # display.scoreboard()

    # Detect Collision with wall
    if snake.head.xcor() > BOUNDARY_POSITIVE or snake.head.xcor() < BOUNDARY_NEGATIVE or snake.head.ycor() > BOUNDARY_POSITIVE or snake.head.ycor() < BOUNDARY_NEGATIVE:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
