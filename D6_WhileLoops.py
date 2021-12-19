'''

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

number_of_hurdles = 6

while number_of_hurdles > 0:
    move()
    do_hurdle()
    number_of_hurdles -= 1

I was looking at this and found a function in the "Reeborg's Keyboard" called at_goal()
Wanted to see if i could make a while loop that would continue the basic pattern until the robot was at the goal.
This is what I came up with to complete the challenge this way. I also found a front_is_clear() function to decide
if the robot should move forward or not.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def do_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        do_hurdle()

while loop syntax:

while something_is_true:
    # do things

It turns out i paused the video before we were given this exact situation where the goal may move. so the at_goal()
function becomes extremely relevant in this scenario. Fortunately, I had already solved for this.

'''