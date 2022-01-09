'''

source: https://app.codingrooms.com/w/selRCZQDMos9

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

Example:

name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53

Print: "Your score is 53."

Hint
The lower() function changes all the letters in a string to lower case.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

'''



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# for testing
# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# we need a score to evaluate our statements
score_true = 0
score_love = 0
score = 0

# we need to know what word we are comparing the names to.


# converting the names to be all lower case.
name1 = name1.lower()
name2 = name2.lower()

# we need to calculate a score.
# calculating for 'true' in name1
score_true += name1.count("t")
score_true += name1.count("r")
score_true += name1.count("u")
score_true += name1.count("e")

# calculating for 'true' in name2
score_true += name2.count("t")
score_true += name2.count("r")
score_true += name2.count("u")
score_true += name2.count("e")

# calculating for "love in name1"
score_love += name1.count("l")
score_love += name1.count("o")
score_love += name1.count("v")
score_love += name1.count("e")


# calculating for "love in name2"
score_love += name2.count("l")
score_love += name2.count("o")
score_love += name2.count("v")
score_love += name2.count("e")

# need to combine scores
score = str(score_true) + str(score_love)
score = int(score)

# need if statements to give an answer.
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 40 and score < 50:
# the line above was my original comparison but pycharm suggested this simplification. 
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
