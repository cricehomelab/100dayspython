'''

BlackJack Goal and basic rules:
Be dealt cards and get to or as close to the number 21 (based on the sum of the cards  you hold) as possible.
If you want another card you HIT
You cannot exceed 21 if you exceed 21 you BUST

The Dealer is also dealt cards and must get as close to 21 as possible.
    Dealer's  first card is revealed to the player but second is hidden.
    Dealer can also HIT
    if the dealer has a score less than 17 they are required HIT

number cards 2,3,4 are worth their face value
Face cards Jack, King and Queen are worth 10 points
Aces are worth either 1 or 11 (counts as a 11 if you are under 21, counts as 1 if you are over 21)


end conditions
if both the dealer and a player have the same score there is a DRAW

some simplified rules we are working with
We are assuming that the ACE is 11 UNLESS the score is over 21
We are assuming that the card pool is infinate (there are an infinite number of every card in the deck)
cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,]

Order of operations
1. Ask if the player wants to play. (yes deal cards) (no end program)
2. Deal the player 2 cards and the dealer 2 cards
    - Show the player both of their cards
    - Show the player the FIRST card the dealer has
3. Ask the player to HIT or STAY
4. If the player decides to hit give them another card
5. If the players hand goes over 21 they lose
6. Allow the player to hit as long as their score is under 21.
7. Once the player stays the dealer needs to make their decision
    - The dealer must hit if their score is under 17
8. Determine who is closest to 21 without going over
    - Declare the winner.

Components:
1. Need a loop to keep the game running
2. Need a way to keep track of card score
3. Need a way to evaluate score



'''

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random

# default card configuration for if the score is under 21
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




game_running = True

# function to get user input
def get_input(question):
    return input(question)

def draw_card():
    return cards[random.randint(0, len(cards)-1)]

def determine_winner(player, dealer):
    # need to take the scores and determine end condition
    if player > 21:
        return "Dealer wins"
    elif dealer > 21:
        return "Player wins"
    else:
        if dealer <=21:
            if dealer > player:
                return "Dealer wins"
            elif dealer == player:
                return "draw"
            else:
                return "Player wins"
        elif player <= 21:
            if player > dealer:
                return "player wins"
            elif dealer > player:
                return "dealer wins"





# function to go through the game
def play_blackjack():
    playing = True
    player_score = 0
    # variable to hold player hand
    player_hand = []
    # draw 2 cards for the player
    player_hand.append(draw_card())
    player_hand.append(draw_card())

    dealer_hand = []
    dealer_hand.append(draw_card())
    dealer_hand.append(draw_card())

    # main loop for player actions
    while playing == True:
        print("_______________")
        print(f"Dealer hand:")
        print(dealer_hand[0])
        print("_______________")

        # calculating score before moving into If statement
        player_score = sum(player_hand)
        # if the score is less than 21 the player can choose to hit or stay
        print("Your hand is:")
        print(player_hand)
        print(f"your score is {player_score} ")
        if player_score < 21:
            action = get_input("Would you like to hit (h) or stay (s)? ")
            # draw a card if the player hits
            if action == "h":
                player_hand.append(draw_card())
            # stay if the player stays
            elif action == 's':
                print(f"You stayed with a score of {player_score}")
                playing = False
            # for invalid choices
            else:
                print("Invalid choice")
        elif player_score == 21:
            print(f"your score is {player_score}")
            playing = False
        elif player_score > 21:
            # need to re-calculate score if there is an ace in player_hand.
            for position, card in enumerate(player_hand):
                if card == 11:
                    player_hand[position] = 1
            if sum(player_hand) > 21:
                print("you bust.")
                playing = False
        # defining computer action
    if player_score <= 21:
        while sum(dealer_hand) < 17:
            dealer_hand.append(draw_card())
        if sum(dealer_hand) > 21:
            print("Dealer busts")
    print("***********************************")
    print("***********************************")
    print(dealer_hand)
    print(f"Dealer score is {sum(dealer_hand)}")
    print(player_hand)
    print(f"player score is {sum(player_hand)}")
    print(determine_winner(sum(player_hand), sum(dealer_hand)))






# Main loop to get the game running.
while game_running == True:
    play_game = get_input("Would you like to play a game of BlackJack? (y or n): ")
    if play_game == 'y':
        play_blackjack()
    elif play_game =='n':
        game_running = False
    else:
        print("Lets try that again...")









