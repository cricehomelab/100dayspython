'''
Rock paper scissors game.

win conditions:
rock beats scissors
scissors beats paper
paper beats rock

tie conditions:
rock ties rock
paper ties paper
scissors ties scissors

other conditions are lose conditions:


How this works.
1.  Ask the player if they want rock paper or scissors. capture in a variable
2.  Have the computer pick randomly.
3.  Display the choices.
3.  Compare the player and computer's choice, and declare a winner.

'''


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# starting the game.
print("Welcome to rock paper scissors.")
print(rock + paper + scissors)

# creating a list to hold the graphics.
choices = [rock, paper, scissors]

# Get the players choice.
player_choice = input("would you like to pick rock(1), paper(2), or scissors(3)?")

# Checking for a valid choice.
if player_choice == "1" or player_choice == "2" or player_choice == "3":
    # convert the player_choice variable to one that will work on the list.
    player_choice = int(player_choice) - 1
# if the choice is not valid the game is over.
else:
    print("You didn't pick a valid choice you lose.")
    # I saw this function and took a guess at what it did, in testing it turned out to work well.
    # For reference: https://pythonguides.com/python-exit-command/#:~:text=exit()%20commands.-,Python%20quit()%20function,be%20used%20in%20the%20interpreter.
    # The above link is for the exit() and quit() functions.
    exit()
# Generate a computer choice, and convert it to one that will work for our list.
computer_choice = random.randint(1, 3) - 1

# print out the selection
print("you play:")
print(choices[player_choice])
print("your opponent plays:")
print(choices[computer_choice])

# check for a win tie or lose
# Win conditions
if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
# Tie Conditions
elif player_choice == 0 and computer_choice == 0:
    print("You tie!")
elif player_choice == 1 and computer_choice == 1:
    print("You tie!")
elif player_choice == 2 and computer_choice == 2:
    print("You tie!")
# any other condition would lose
else:
    print("You lose!")
