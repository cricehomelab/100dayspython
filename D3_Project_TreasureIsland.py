print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# this is the flowchart we need to use to fulfill the conditions.
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You follow a path into the woods, after some time the path branches in two directions.")
beach = input("Would you like to go left or right (l or r)? \n")
beach = beach.lower()
if beach == 'l':
    # advance to next area
    print("Following the trail, you come to a river that you will need to cross. There seems to be a dock.")
    dock = input("would you like to swim across the river or wait and see what happens (s or w)? \n")
    dock = dock.lower()
    if dock == "w":
        # advance to next area
        print("Your patience pays off. A ferryman and his ferry come and dock at the river.")
        print("She offers to take you across the river, and you accept.")
        print("Once you make it across the river there is a small empty village with 3 houses")
        print("One of the doors is yellow (y).")
        print("One of the doors is blue (b).")
        print("One of the doors is red (r).")
        village = input("Which door would you like to go into (y, b, or r)? \n")
        village = village.lower()
        if village == 'y':
            # win condition.
            print("In this room you find a chest full of treasure.")
            print("You win!")
        elif village == 'r':
            print("You walk into the room the door locks behind you.")
            print("You smell Kerosene and a torch falls from a hole in the ceiling.")
            print("The room is engulfed in flames and you cannot escape.")
            print("You burn to death.")
            print("Game over.")
        elif village == 'b':
            print("You walk through the blue door.")
            print("The door closes and locks behind you.")
            print("there are cages at the corners of the room.")
            print("They slowly open revealing wild beasts.")
            print("They charge you and attack you.")
            print("You die, and the beasts devour you.")
            print("Game over.")
        else:
            print("that wasn't an option. Zeus smites you with lightening.")
            print("Game over.")
    elif beach == 's':
        # game over
        print("Your swim starts out strong, but the current is pulling you down river very quickly.")
        print("Your strength gives out and you are pulled under. You drown.")
        print("Game over.")
    else:
        print("that wasn't an option. Zeus smites you with lightening.")
        print("Game over.")
else:
    # Game over.
    print("You walk but fall into a hole that was obviously a trap. You die.")
    print("Game over.")
