
'''
Original Concept:
The original idea of this challenge it to "hide" a treasure chest on a grid.

New Concept:
To make it more like a game. The new idea on this concept is to have the computer "hide" the treasure and for the
player to guess where it is.

Grid layout
        1  2  3   column x
  1    [ ][ ][ ]
  2    [ ][ ][ ]
  3    [ ][ ][ ]
rows y

The input will be a 2 digit number that specifies the column then the row.
From the input the program will place an x in that position.
example input 23
There is a test to check if that is the location where the treasure is hidden and if that is the position there will be
win  condition if there is nothing there there will be an O placed there to indicate that space has been checked.

Win condition if 23 is the correct location
        1  2  3   column x
  1    [ ][ ][ ]
  2    [ ][ ][ ]
  3    [ ][X][ ]
rows y

Unsuccessful attempt to guess the location.

        1  2  3   column x
  1    [ ][ ][ ]
  2    [ ][ ][ ]
  3    [ ][O][ ]
rows y


Things to change:
 the computer hide the treasure secretly.
     Use randomint to get numbers for where the treasure is hidden.
Change the input to a guess where the treasure is.
Win condition made to find the treasure.
Made this into a function for future use of this minigame.
Added error handling to prevent an out of range issue if the wrong buttons are selected.

'''
import random

def treasure_find():
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    map = [row1, row2, row3]

    # Variable to keep the loop going and  to determine when a "win" condition happens.
    treasure_found = False
    # this is the column position of the treasure.
    treasure_x = random.randint(0, 2)
    # this is the row position of the treasure.
    treasure_y = random.randint(0, 2)

    # This is the main game loop.
    while treasure_found == False:
        print("There is treasure in this room. Look around and find it")
        print("Pick a row then a column to check for the treasure.")
        print("Example guess would be 11, 22, or 32")
        print(f"{row1}\n{row2}\n{row3}")
        position = input("Where do you want to look for the treasure? ")

        # converting the rows the player knows to the correct index positions.
        position_y = int(position[1]) - 1
        position_x = int(position[0]) - 1

        # going to add error handling if someone puts in an invalid input.
        possible_positions = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        # if statement to check for valid guesses.
        if position in possible_positions:
            # keeping the console window clean.
            print("\n" * 15)
            # checking for a win condition.
            if position_x == treasure_x and position_y == treasure_y:
                # if the treasure is found
                # Replacing the "⬜️" with "X"
                map[position_y][position_x] = 'X️'
                treasure_found = True
            # action for if there is not a win here.
            else:
            # if nothing is found at the location
                map[position_y][position_x] = 'O️'
        else:
            print("That is not a valid position.")
    print("You found the treasure!")
    print(f"{row1}\n{row2}\n{row3}")

treasure_find()




