"""
This is a bit later after the requirements were fully provided the d18_main.py was really just a stab in the
dark at the project and seeing what I could do with it. This path worked quite well also and was easier to
accomplish after just playing around at it

1. 10/10 dot matrix
2. Dot should be 20 in size.
3. spacing should be 50.

"""

import random
import turtle as t
#import colorgram

rgb_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73),(47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

# colors = colorgram.extract('d18_hisrt_example.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# creating turtle object
pen = t.Turtle()
# creating screen object
screen = t.Screen()
# window size
width = 910
height = 900

# setting the window size
screen.setup(width=width, height=height, startx=0, starty=0)

# set turtle speed
pen.speed(0)

# Set RGB color mode
t.colormode(255)

# make pen invisible
pen.hideturtle()

# dot spacing
distance_x = 90
distance_y = 90

x_coord = -425
y_coord = -425

# turtle starting location
pen.up()
pen.setx(x_coord)
pen.sety(y_coord)


def draw_x(x, distance):
    """
    This draws a line of dots.

    :param x: the current x coordinate
    :param distance: distance between dots drawn
    :return: None
    """
    #print(x)
    for _ in range(10):
        pen.setx(x)
        pen.down()
        pen.color(random.choice(rgb_colors))
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.up()
        x += distance
        pen.setx(x)


for _ in range(10):
    draw_x(x_coord, distance_x)
    y_coord += distance_y
    pen.sety(y_coord)


screen.exitonclick()
