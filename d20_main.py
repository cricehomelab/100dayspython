import d20_snake
import time
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Let's Play a game of Snake.")
screen.tracer(0)

snake = d20_snake.Snake()
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


screen.exitonclick()

