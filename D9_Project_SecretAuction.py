'''

Run in a while loop
1. ask for a name
2. ask for a bid
3. append user and bid to a list
4. ask if there is another bid.
5. If yes, clear screen.
6. repeat steps 1-5 until all bids are captured.

Determine the winner of the bid
1. loop through list.
2. determine which bid is highest.
3. display the winner.

Things we need.
1. Dictionary to hold a name and a bid
2. loop to add to the dictionary
3. way to determine that all bidding is complete
4. way to determine who is the highest bidder
5. method to clear the screen between bids.

'''

import D9_Gavel



# variable for while loop below to keep bidding open
bidding_open = True
bids = {}

# this is an initial way to clear the screen to allow for consistency in where the typing is below.
# the other non-replit methods of clearing the screen i found were not working for me.
# this seemed to be the best way I could do this for now.
def clear_screen():
    for i in range(50):
        print()

# function to get and add a bid to the bids dictionary.
def get_bid():
    name = input("Please enter your name? ")
    bid = int(input("Please enter your bid? $"))
    # add name and bid to the dictionary.
    bids[name] = bid

# this function determines the winner of the silent auction.
def determine_winner(list_of_bids):
    clear_screen()
    top_bid = 0
    for entry in list_of_bids:
        if list_of_bids[entry] > top_bid:
            top_bid = list_of_bids[entry]
    for entry in list_of_bids:
        if top_bid == list_of_bids[entry]:
            print(f"The winner is {entry}, with a bid of ${list_of_bids[entry]}.")

# putting this in for consistency
clear_screen()
# here is the ascii art that is part of the project.
print(D9_Gavel.logo)
# getting the initial bid.
get_bid()
# while loop to get any additional bids.
while bidding_open:
    continue_bidding = input("Is there another bid? (yes or no) \n")
    if continue_bidding == "no":
        # end bidding phase
        bidding_open = False
    elif continue_bidding == "yes":
        # clear screen
        clear_screen()
        get_bid()
    # catches invalid answers to the yes/no question.
    else:
        print("That was not a valid answer.")

determine_winner(bids)

