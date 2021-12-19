'''

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

Goal in this scenario is to get the robot across to a finish point
While navigating around some hurdles.

Here is an ascii representation of the grid we are needing to get around
S = start point
F = finish point

3
2         |       |       |       |        |        |
1   S     |       |       |       |        |        |  F
    1   2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |12 | 13

First attempt:
I defined a function named do_hurdle() that does the steps needed to do a hurdle and face our next objective.
I then manually commanded out the steps needed to step through the desired path.

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this is a function that does all the steps of a single hurdle.
def do_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

move()
do_hurdle()
move()
do_hurdle()
move()
do_hurdle()
move()
do_hurdle()
move()
do_hurdle()
move()
do_hurdle()

Second attempt:
I liked the do_hurdle() function, but it ocured to me, and I think in part due to the lecture verbiage (pre-solution we
could use a forloop here, so I tried to implement that. Since there are 6 hurdles I should be able to define a range
and have the robot go in a looping fashion to get to the objective. 

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this is a function that does all the steps of a single hurdle.
def do_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for hurdles in range(6):
    move()
    do_hurdle()

'''