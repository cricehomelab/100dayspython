'''

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
This is a maze challenge the goal was to navigate a maze to get to a destination.

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    # the main idea is to go right if we can. so if the right is clear we want to turn that way and move.
    if right_is_clear():
        turn_right()
        move()
    # this will happen if moving right is not an option, and you can move foward.
    elif front_is_clear():
        move()
    # this will turn left if you cannot move forward or to the right.
    else:
        turn_left()

'''