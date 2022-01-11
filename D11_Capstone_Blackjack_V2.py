'''
While the previous iteration technically did what we wanted. I noticed I did not follow some rules quite as
intended. This is my second look at the code I wanted it to be versioned for comparison.

1 - I found some issues with the algorithm i was using for the dealer turn. It looked like it was busting way more than it
should. I found that i was not re-calculating for the wild card 11. I fixed this.
2 - added a "rules" section for players.
3 - formatted some code to do the same thing but feel more readable, for me at least.
4 - did not take into account that the dealer must play even if the player busts. Added logic to account for that.
5 - fixed win conditions to take into account that the dealer must play.
6 - removed some unused variables and some commented out print statements.
7 - found some code that would never run or were unnecessary, removed that.
'''

import random

# default card configuration
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_rules():
    """get_rules() ouputs the rules for the player"""
    print("The deck is unlimited in size.")
    print("There are no jokers.")
    print("The Jack/Queen/King all count as 10, and are displayed as 10.")
    print("The the Ace can count as 11 or 1. They display as 11 until 21 is exceeded then count as 1.")
    print("Cards are not removed from the deck as they are drawn.")
    print("If you bust (go over 21) you lose.")
    print("The dealer must hit below 17.")
    print("If the dealer score is the same as the player score there is a draw.")
    print("The objective is to have a score of 21, or be closer to 21 then the dealer without exceeding a score of 21.")


def get_input(question):
    """get_input(question) takes one string where the string is a prompt this returns an answer."""
    return input(question)


def draw_card():
    """draw_card() draws a card for either player returns the card value"""
    return cards[random.randint(0, len(cards) - 1)]


def determine_winner(player, dealer):
    """determine_winner(player, dealer) this takes 2 int inputs, the player score and the dealer score and determines
       who the winner is. """
    # need to take the scores and determine end condition
    # Dealer bust scenario
    if dealer > 21:
        return "The Dealer busted, you win!"
    # Player bust scenario
    elif player > 21:
        return "You Bust, the Dealer wins... Better luck next time."
    # other situations.
    else:
        if dealer > player:
            return "Dealer wins"
            # if scores are the same there is a draw
        elif dealer == player:
            return "draw"
            # this would only be player > dealer
        else:
            return "You win!"


# function to go through the game
def play_blackjack():
    """play_blackjack() This is the main loop for running the game. """
    playing = True
    # variable to hold player hand
    player_hand = []
    # draw 2 cards for the player
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    # draw 2 cards for the dealer
    dealer_hand = []
    dealer_hand.append(draw_card())
    dealer_hand.append(draw_card())

    # main loop for player actions
    while playing:
        print("_______________")
        print(f"Dealer hand:")
        print(dealer_hand[0])
        print("_______________")

        # calculating score before moving into If statement
        player_score = sum(player_hand)

        # display the player what their hand is and what their score is.
        print("Your hand is:")
        print(player_hand)
        print(f"your score is {player_score} ")
        # if the score is less than 21 the player can choose to hit or stay
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
            playing = False
        elif player_score > 21:
            # need to re-calculate score if there is an ace in player_hand.
            for position, card in enumerate(player_hand):
                if card == 11:
                    print("11 is wild recalculating score...")
                    player_hand[position] = 1
            if sum(player_hand) > 21:
                print("you bust.")
                playing = False
    # defining computer action
    dealer_turn = True
    while dealer_turn:
        # if the player score is over 21 the dealer does not need to take action.
        # if player_score <= 21:
        # the dealer must hit if they are under or at 17 per the rules.
        if sum(dealer_hand) <= 17:
            dealer_hand.append(draw_card())
        # if the dealer hand is over 21 the dealer busts, but if they have an ace (11) it should recalculate their
        # score to account for the wild card.
        elif sum(dealer_hand) > 21:
            for position, card in enumerate(dealer_hand):
                if card == 11:
                    print("Dealer has wild card 11 recalculating score...")
                    dealer_hand[position] = 1
            if sum(dealer_hand) > 21:
                dealer_turn = False
        elif sum(dealer_hand) == 21:
            dealer_turn = False
        else:
            dealer_turn = False

    print("***********************************")
    print("***********************************")
    print(dealer_hand)
    print(f"Dealer score is {sum(dealer_hand)}")
    print(player_hand)
    print(f"player score is {sum(player_hand)}")
    print(determine_winner(sum(player_hand), sum(dealer_hand)))


game_running = True
# Main loop to get the game running.
while game_running:
    print("Welcome to Blackjack!")
    print("Press r for the rules.")
    play_game = get_input("Would you like to play a game of BlackJack? (y or n): ")
    if play_game == 'y':
        play_blackjack()
    elif play_game == 'n':
        game_running = False
    elif play_game == 'r':
        get_rules()
    else:
        print("Lets try that again...")
