"""

The goal here is to make my Blackjack game more modular IE breaks down the components more into functions

Components of a player turn
1. Show player their cards and give them their score
2. Programmatically check to make sure their score is not over 21
    A. Check for wild cards recalculate if needed
3. Ask player for their input.

Components of a Dealer turn
1. provide dealer with their score
2. Programmatically check to make sure their score is not over 21
    A. Check for wild cards recalculate if needed
3. Let dealer logic decide what to do.

Components of a game
1. Let player make their moves
2. Let dealer make their moves
3. Calculate a winner.

I was able to refactor my code here while keeping the same rules as before but breaking out some elements that were
repeated in code.

- wild_ace(hand) is a function that recalculates the score when wild cards occurred, previously this happened outside
a function in both the dealer and player turns.

- dealer_turn(dealer) this function handles the entire dealer turn.

- player_turn(hand, dealer) this function handles the player's turn programmatically.

- join_table() is a function that runs one round of the game.

- game_start() is a function that will start the game.

- added get_record() function to display how many wins, losses, and draws a user has.

- I added variables to help to keep track of wins, loses, and draws as well.

"""

import random

# default card configuration
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# variable to keep game running
running = True


def get_input(question):
    """get_input(question) takes one string where the string is a prompt this returns an answer."""
    return input(question)


def show_hands(player, dealer):
    """show_hands(player, dealer) takes the hands in a player and dealer deck and displays them appropriately"""
    print("_______________")
    print(f"Dealer hand:")
    print(f"[{dealer[0]}, X]")
    print("_______________")
    print("Your hand is:")
    print(player)
    print(f"your score is {sum(player)} ")


def dealer_turn(dealer):
    """dealer_turn() handles the dealer turn"""
    dealers_turn = True
    while dealers_turn:
        # if the player score is over 21 the dealer does not need to take action.
        # if player_score <= 21:
        # the dealer must hit if they are under or at 17 per the rules.
        if sum(dealer) <= 17:
            dealer.append(draw_card())
        # if the dealer hand is over 21 the dealer busts, but if they have an ace (11) it should recalculate their
        # score to account for the wild card.
        elif sum(dealer) > 21:
            dealer = wild_ace(dealer)
            if sum(dealer) > 21:
                return dealer
        elif sum(dealer) == 21:
            return dealer
        else:
            return dealer


def player_turn(hand, dealer):
    """player_turn() performs a turn for a player"""
    print("player takes their turn.")
    playing = True
    while playing:
        show_hands(hand, dealer)
        if sum(hand) < 21:
            action = get_input("Would you like to hit (h) or stay (s)? ")
            # draw a card if the player hits
            if action == "h":
                hand.append(draw_card())
            # stay if the player stays
            elif action == 's':
                return hand
            # for invalid choices
            else:
                print("Invalid choice")
        elif sum(hand) == 21:
            return hand
        elif sum(hand) > 21:
            # need to re-calculate score if there is an ace in player_hand.
            hand = wild_ace(hand)
            if sum(hand) > 21:
                return hand


def draw_card():
    """draw_card() picks a card from the 'cards' list. """
    return cards[random.randint(0, len(cards) - 1)]


def wild_ace(hand):
    """wild_ace(hand) takes a list as input, checks it for aces, and re-calculates the 11 to 1's."""
    for position, card in enumerate(hand):
        if card == 11:
            print("11 is wild recalculating score...")
            hand[position] = 1
    return hand


def determine_winner(player, dealer):
    """determine_winner(player, dealer) takes the scores offered it and determines a win/lose/draw condition"""
    # need to take the scores and determine end condition
    # Dealer bust scenario
    print(f"You end with a hand of {player}, and a score of {sum(player)}.")
    print(f"The dealer ends with a hand of {dealer}, and a score of {sum(dealer)}.")
    if sum(dealer) > 21:
        return "The Dealer busted, you win!", "win"
    # Player bust scenario
    elif sum(player) > 21:
        return "You Bust, the Dealer wins... Better luck next time.", "dealer"
    # other situations.
    else:
        if sum(dealer) > sum(player):
            return "The Dealer wins", "dealer"
            # if scores are the same there is a draw
        elif sum(dealer) == sum(player):
            return "The game ends as a draw.", "draw"
            # this would only be player > dealer
        else:
            return "You win!", "win"


def join_table():
    """join_table() runs one round of the game."""
    player_hand = []
    dealer_hand = []
    # draw 2 cards for the player
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    # draw 2 cards for the dealer
    dealer_hand.append(draw_card())
    dealer_hand.append(draw_card())
    player_hand = player_turn(player_hand, dealer_hand)
    dealer_hand = dealer_turn(dealer_hand)
    return determine_winner(player_hand, dealer_hand)


def get_rules():
    """get_rules() outputs the rules for the player"""
    print("The deck is unlimited in size.")
    print("There are no jokers.")
    print("The Jack/Queen/King all count as 10, and are displayed as 10.")
    print("The the Ace can count as 11 or 1. They display as 11 until 21 is exceeded then count as 1.")
    print("Cards are not removed from the deck as they are drawn.")
    print("If you bust (go over 21) you lose.")
    print("The dealer must hit below 17.")
    print("If the dealer score is the same as the player score there is a draw.")
    print("The objective is to have a score of 21, or be closer to 21 then the dealer without exceeding a score of 21.")


def get_record(win, lose, draw):
    print(f"you have won {win} games.")
    print(f"you have lost {lose} games.")
    print(f"you have {draw} draws.")


def game_start():
    """game_start() is what starts and keeps the game running."""
    win = 0
    lose = 0
    draw = 0
    game_running = True
    print("Welcome to Blackjack!")
    print("Press r for the rules.")
    while game_running:
        logic = ["", 0]
        play_game = get_input("Would you like to play a game of BlackJack? (y or n), or w for your record: ")
        if play_game == 'y':
            logic = join_table()
        elif play_game == 'n':
            game_running = False
        elif play_game == 'r':
            get_rules()
        elif play_game == 'w':
            get_record(win, lose, draw)
        else:
            print("Lets try that again...")
        print(logic[0])
        if logic[1] == "win":
            win += 1
        elif logic[1] == "dealer":
            lose += 1
        elif logic[1] == "draw":
            draw += 1


game_start()
