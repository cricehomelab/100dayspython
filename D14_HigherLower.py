'''

2022-01-21
Initial thoughts: I had some trouble breaking out into smaller functions, so I ended up getting this to work I think with
2 functions. One to run the game and one to check the answer. I am going to sleep on it from here, and see if fresh
eyes give me a better view in the AM.

'''

import D14_Art
import D14_Game_data
import random


def check_answer(first, second, answer):
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


def play_game():
    count = 0
    playing = True
    while playing:
        if count == 0:
            person_1 = random.choice(D14_Game_data.data)
        else:
            person_1 = person_2
        person_2 = random.choice(D14_Game_data.data)
        while person_2['name'] == person_1['name']:
            person_2 = random.choice(D14_Game_data.data)
        answering = True
        while answering:
            print(f"Does {person_1['name']} a {person_1['description']} from {person_1['country']} have more "
                  f"followers than...")
            print(D14_Art.vs)
            print(f"{person_2['name']} a {person_2['description']} from {person_2['country']}???")
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
