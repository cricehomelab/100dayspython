'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
This is the same code from the hurdles2 challenge, but it turns out i accidently solved for hurdles 3 in that one as
well.

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

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
Hurdles 4 has variable hurdle heights so this should require changing my code.
The change I had to make here was to my do_hurdle function to account for the variable height of the hurdles.
using the wall_on_right() function it allowed the robot to determine how high up it should go.
using the front_is_clear() function it allowed me to stop moving down when the robot got back to the bottom square.

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this is a function that does all the steps of a
# single hurdle.
def do_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        do_hurdle()

apparently there is an infinate loop possibility here that con happen I had run the previous itteration around 10 times
and did not encounter this scenario, but on seeing it demonstrated i thought of a possible solution to break it out of
a loop.

Essentially, if the robot turns right more than 4 times in a row the robot will instead turn left.
If the robot goes a direction other than right it resets a variable i named right_turns back to 0.
Using the worlds that were provided in the course with the added code it looks like all of those were able to be completed.

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this keeps track of how many right turns have been made.
right_turns = 0

while not at_goal():
    # this is the condition to turn left if there have been 4 or more right turns.
    if right_turns > 4:
        turn_left()
        # reset the right turn counter.
        right_turns = 0
    elif right_is_clear():
        turn_right()
        move()
        # adding to keep track of how many right turns have been made.
        right_turns += 1
    elif front_is_clear():
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0

'''
