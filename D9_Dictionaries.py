'''

Dictionaries are composed of keys and values

Example:
KEY         VALUE
bug         an error in the program that prevents the program from running as expected.
function    a piece of code you can easily call over and over again.
loop        the action of doing something over and over again.

{Key: Value}
{
"Bug": "an error in the program that prevents the program from running as expected.",
"Function": "a piece of code you can easily call over and over again.",
"Loop": "the action of doing something over and over again"
}

'''

programming_dictionary = {
    "Bug": "an error in the program that prevents the program from running as expected.",
    "Function": "a piece of code you can easily call over and over again.",

}

# Retrieving items from a dictionary.
print(programming_dictionary["Bug"])

# adding new items to a dictionary.
programming_dictionary["Loop"] = "the action of doing something over and over again"

print(programming_dictionary)

# Creating an empty list
empty_list = []

# Creating an empty dictionary
empty_dictionary = {}

# wiping the contents of a dictionary.
# programming_dictionary = {}

print(programming_dictionary)

# Editing an item in a dictionary.
programming_dictionary["Bug"] = "An error in the program. Things don't work right!"

print(programming_dictionary)

# Looping through a dictionary.
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")
