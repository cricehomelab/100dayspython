
'''

after working though the easy solution on what I already knew and having to look up a few things for the hard solution
I decided to try and go back and simplify the whole thing.

Using the random.shuffle() function made this all a WHOLE lot easier.

'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Changing this to set how long the password should be.
nr_length = int(input("How many characters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Getting how many letters based on the length minus the symbols and numbers
nr_letters = nr_length - (nr_symbols + nr_numbers)

letters_length = len(letters) - 1
numbers_length = len(numbers) - 1
symbols_length = len(symbols) - 1

password_easy = ""
password_hard = ""
list_of_characters = []

for letter in range(0, nr_letters):
    randomnum = random.randint(0, letters_length)
    list_of_characters.append(letters[randomnum])
# get a random number for each number we want in our password
for number in range(0, nr_numbers):
    randomnum = random.randint(0, numbers_length)
    list_of_characters.append(numbers[randomnum])
# get a random symbol for each symbol we want in our password.
for symbol in range(0, nr_symbols):
    randomnum = random.randint(0, symbols_length)
    list_of_characters.append(symbols[randomnum])

# This is the password list generate in sequence.
password_easy = password_easy.join(list_of_characters)
# the random.shuffle randomizes the list of characters.
random.shuffle(list_of_characters)
# this will be the password with the letters characters and numbers out of sequence
# this makes it more random.
password_hard = password_hard.join(list_of_characters)

print(f"easy answer for password generator is: {password_easy}")
print(f"hard answer for password generator is: {password_hard}")
