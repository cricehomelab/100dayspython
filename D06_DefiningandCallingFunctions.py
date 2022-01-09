'''

examples of functions we have used
print()
len()
int()

functions can be seen with the function_name and a parenthesis after it ().

creating a function is done with the "def" keyword

'''

# creating a function.
def my_function():
    # Indent to show the program what the function does.
    print("This is a function.")

# Executing the function we created.
my_function()

# This function just prints out something but functions usually solve for an issue in a program.

'''

We are starting to use a robot tool call reboorg's world. Linke below:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
in this game we can use python like code to manipulate the movement of a robot. 
We created a function to make the robot make a right turn and to do a 180 degree turn to reverse. 

Below is the code to do the right turn and the 180 degree turn. 
There is also a challenge to make the robot do a small square on the grid provided by the application. 

# function to turn robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# function to turn robot 180 degrees
def turn_around():
    turn_left()
    turn_left()

# Challenge is to draw a square
# 1-1 to 2-1
# 2-1 to 2-2
# 2-2 to 1-2
# 1-2 to 1-1

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()





'''
