'''

2022-01-22
After thinking about it and looking for more things to break out the only real places I saw an opportunity was with
getting the comparison for the game, and for displaying the question for the user.

'''

import D14_Art
import D14_Game_data
import random


def check_answer(first, second, answer):
    """check_answer(first, second, answer) takes 2 comparison dictionaries to see which of these have the most followers
    then it compares the answer the user put in to see if the user guessed the correct user with the most followers.
    This returns 1 for correct guesses, so it can be added to the player score if they guessed correctly. It does not
    return anything if the user is incorrect."""
    if answer == 'y' and first['follower_count'] > second['follower_count']:
        print("you are correct.")
        return 1
    elif answer == 'y' and first['follower_count'] < second['follower_count']:
        print("you are incorrect.")
    elif answer == 'n' and first['follower_count'] > second['follower_count']:
        print("you are incorrect.")
    elif answer == 'n' and first['follower_count'] < second['follower_count']:
        print("you are correct.")
        return 1


def get_people(count):
    """get_people(count) take an int count to see if the user is on a streak of 1 or greater to see how it should
    get additional people if the streak is 0 it needs to get 2 people if the streak is greater than that it needs
    to get 1 person and make the second person """
    person_2 = {}
    if count == 0:
        person_1 = random.choice(D14_Game_data.data)
    else:
        person_1 = person_2
    person_2 = random.choice(D14_Game_data.data)
    while person_2['name'] == person_1['name']:
        person_2 = random.choice(D14_Game_data.data)
    return person_1, person_2


def show_question(person_1, person_2):
    """Displays the comparison question for the user."""
    print(f"Does {person_1['name']} a {person_1['description']} from {person_1['country']} have more "
          f"followers than...")
    print(D14_Art.vs)
    print(f"{person_2['name']} a {person_2['description']} from {person_2['country']}???")


def play_game():
    """main game loop for the higher lower game."""
    count = 0
    playing = True
    while playing:
        comparison = get_people(count)
        person_1 = comparison[0]
        person_2 = comparison[1]
        # this was removed into the get_people(count) function.
        #if count == 0:
        #    person_1 = random.choice(D14_Game_data.data)
        #else:
        #    person_1 = person_2
        #person_2 = random.choice(D14_Game_data.data)
        #while person_2['name'] == person_1['name']:
        #    person_2 = random.choice(D14_Game_data.data)
        answering = True
        while answering:
            # put this into the function show_question()
            #print(f"Does {person_1['name']} a {person_1['description']} from {person_1['country']} have more "
            #      f"followers than...")
            #print(D14_Art.vs)
            #print(f"{person_2['name']} a {person_2['description']} from {person_2['country']}???")
            show_question(person_1, person_2)
            response = input('y for yes, n for no: \n')
            if response == 'y' or response == 'n':
                win = check_answer(person_1, person_2, response)
                answering = False
                if win == 1:
                    count += 1
                    print(f"Your score is {count}")
                else:
                    print(f"You lose your streak was {count}")
                    return
            else:
                print("invalid response.")


print(D14_Art.logo)
play_game()
