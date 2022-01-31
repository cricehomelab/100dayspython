'''
This was the main challenge.

1. extract the color palette used by Damien Hirst (https://en.wikipedia.org/wiki/Damien_Hirst) to make one of his
paintings.
2. make a "painting" similar to his painting in turtle.

I did a lot of this before following along in the video. I paused at the first challenge point and tried to create the
painting without further assistance. I will make a separate .py to go through the instructor lead challenges.

While this code worked it didn't hit all the requirements the instructor gave us later. I still think this code
is valid, but its more along the lines of scratch work when compared to d18_instructor_led.py.

'''

import colorgram
import random
import turtle as t

t.colormode(255)

rgb_colors = []
colors = colorgram.extract('d18_hisrt_example.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

# creating turtle object
pen = t.Turtle()
# creating screen object
screen = t.Screen()
# window size
width = 1600
height = 900
# setting the window size
screen.setup(width=width, height=height, startx=0, starty=0)

# set turtle speed
pen.speed(0)

# dot spacing
distance_x = 100
distance_y = 100

# set the location of x and y coordinates
location_x = -width / 2 + 50
location_y = -height / 2 + 50

# turtle starting location
pen.up()
pen.setx(location_x)
pen.sety(location_y)


def draw_x(x, distance):
    """
    This draws a line of dots.

    :param x: the current x coordinate
    :param distance: distance between dots drawn
    :return: None
    """
    #print(x)
    for _ in range(int(width / distance_x)):
        pen.setx(x)
        pen.down()
        pen.color(random.choice(rgb_colors))
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.up()
        x += distance
        pen.setx(x)


for _ in range(int(height / distance_y)):
    draw_x(location_x, distance_x)
    location_y += distance_y
    pen.sety(location_y)


screen.exitonclick()
