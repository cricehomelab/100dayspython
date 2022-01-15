# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import D12_art


def check_guess(number, secret_number):
    """check_guess(number, secret_number compares the player guess, number, to the secret number generated.
    Evaluates if the number == secret_number and returns if it was correct. If it is not correct it returns whether
    the guess is higher or lower than the secret_number. """
    if secret_number == number:
        print(f"the correct answer was {secret_number}")
        return "You win."
    elif secret_number > number:
        return f"the secret number is higher than {number}."
    elif secret_number < number:
        return f"the secret number is lower than {number}."


def get_difficulty():
    """get_difficulty() asks the player what difficulty they want to play at and returns the number of turns
    for the difficulty they picked."""
    dif = input("would you like to play as easy or hard? (e or h) : ")
    if dif == "e":
        return 10
    elif dif == "h":
        return 5


def get_number():
    """get_number() returns a random number. """
    return random.randint(1, 100)


def guess():
    """guess() this takes an input and makes sure it is valid. It returns a valid guess."""
    while True:
        player_guess = input("What is your guess? : ")
        if 0 < int(player_guess) < 101:
            return int(player_guess)
        else:
            print("that was not a valid guess.")


def start_game(turns):
    """start_game(turns) takes the input turns to determine how many attempts a player has to guess the answer. This
    will run the main game loop."""
    secret_number = get_number()
    turns_left = turns
    print("I am thinking of a number between 1 and 100.")
    while turns_left > 0:
        player_guess = guess()
        response = check_guess(player_guess, secret_number)
        print(response)
        if response == "You win.":
            return
        else:
            turns_left -= 1
            print(f"wrong you have {turns_left} turns left...")


print(D12_art.logo)
# this is a loop to let the user play multiple games in a row.
game_running = True
while game_running:
    play_game = input("would you like to play a game of higher or lower? (y or n) : ")
    if play_game == "y":
        start_game(get_difficulty())
    elif play_game == "n":
        game_running = False
    else:
        print("I'm not sure I understand your answer...")
