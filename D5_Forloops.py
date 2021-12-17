'''

For Loop
example in pseudo code

for item in list_of_items:
    do something to each item in the list.

'''

fruits = ['Apple', 'Peach', 'Pear', 'Watermelon']

# This iterates through the list of fruits we made and prints out each individual fruit in fruits.
print("Printing all the items in fruit.")
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie.")

# Self check after looking at the basic of it want to see if I can isolate out parts of the list.
# Just for simplicity I want to see if I can print specific items IE any fruit starting with the letter 'p'.
print("printing all the fruits in the list that start with 'p'.")
for fruit in fruits:
    if fruit[0].lower() == "p":
        print(fruit)

