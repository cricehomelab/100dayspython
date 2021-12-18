
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Changing this to set how long the password should be.
nr_length = int(input("How many characters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Getting how many letters based on the length minus the symbols and numbers
nr_letters = nr_length - (nr_symbols + nr_numbers)

print(f"Generating a password with {nr_letters} letters, {nr_numbers} numbers, and {nr_symbols} symbols.")
print(f"The password will be {nr_length} characters long.")

letters_length = len(letters) - 1
numbers_length = len(numbers) - 1
symbols_length = len(symbols) - 1


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''
Easy way:
1. Need to find out what kind of password someone wants, how long, how many numbers, how many characters.
2. Need to figure out how many letters should be there based on how many numbers and symbols they want.
3. Need to generate a passsword based on those specifications. (need to break this down more).
    A. Need to randomly get letters for the password and append them.
    B. Need to randomly get numbers for the password and append them.
    C. Need to randomly get characters for the password and append them.

'''

# first attempt at the easy method.
password_easy = ""

# get a random letter for the number of letters we want in our password
for letter in range(0, nr_letters):
    randomnum = random.randint(0, letters_length)
    password_easy += letters[randomnum]
# get a random number for each number we want in our password
for number in range(0, nr_numbers):
    randomnum = random.randint(0, numbers_length)
    password_easy += str(numbers[randomnum])
# geta random symbol for each symbol we want in our password.
for symbol in range(0, nr_symbols):
    randomnum = random.randint(0, symbols_length)
    password_easy += str(symbols[randomnum])
print("results of the Eazy test.")
print("The order of characters is not randomized.")
print(password_easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
'''
1. Need to find out what kind of password someone wants, how long, how many numbers, how many characters.
2. Need to figure out how many letters should be there based on how many numbers and symbols they want.
3. Need to generate a list of letters, symbols, and numbers for our password. 
    A. Need to randomly get letters for the password and append them to a list
    B. Need to randomly get numbers for the password and append them to a list.
    C. Need to randomly get characters for the password and append them to a list.
4. Need to use each item in our list only once to generate a password. 

'''

password_hard = ""
characters_for_password = []
# Generate a list of characters to be used in the password.
# get a random letter for each letter we want in our password.
for letter in range(0, nr_letters):
    randomnum = random.randint(0, letters_length)
    characters_for_password.append(letters[randomnum])
# get a random number for each number we want in our password
for number in range(0, nr_numbers):
    randomnum = random.randint(0, numbers_length)
    characters_for_password.append(numbers[randomnum])
# get a random symbol for each symbol we want in our password.
for symbol in range(0, nr_symbols):
    randomnum = random.randint(0, symbols_length)
    characters_for_password.append(symbols[randomnum])

random.shuffle(characters_for_password)
password_hard = password_hard.join(characters_for_password)
print(password_hard)

