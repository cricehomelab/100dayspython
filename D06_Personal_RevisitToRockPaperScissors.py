'''
Rock paper scissors game. version 2
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
1.  Start the gameplay loop.
2.  Ask the player if they want rock paper or scissors. capture in a variable
3.  Have the computer pick randomly.
4.  Display the choices.
5.  Compare the player and computer's choice, and declare a winner.
6.  Program goes back to the start of the while loop.

20211219 - Adding a while loop so the game can be played more times than once. I had to change the way my if else
           worked here so it would not end with an error if we quit the game.

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

# condition to keep the game running.
game_running = True

# initializing a while loop to keep the game running.
while game_running == True:
    # Get the players choice.

    player_choice = input("would you like to pick rock(1), paper(2), scissors(3) or type anything else to quit?")

    # Checking for a valid choice.
    if player_choice == "1" or player_choice == "2" or player_choice == "3":
        # convert the player_choice variable to one that will work on the list.
        player_choice = int(player_choice) - 1
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
    # if the choice is not valid the game is over.
    else:
        print("You exit the game.")
        game_running = False

