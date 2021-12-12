


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# index out of range error will show here because the there is no item 50 this list starts at 0 and goes to 49.
#print(states_of_america[50])
'''
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day4Python/D4_IndexErrorsAndNestedLists.py", line 13, in <module>
    print(states_of_america[50])
IndexError: list index out of range
'''
# to get the correct 50th state in this example you will need to print position 49
print(states_of_america[49])

# gets the length of the list. (answer here will be 50)
num_of_states = len(states_of_america)
print(num_of_states)
# this will give you an index error
# print(states_of_america[num_of_states])
# this is how it will not throw an index error
print(states_of_america[num_of_states - 1])

# List of fruits studied to be found with high amounts of pesticide in them.
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]
# Since this list contains fruits and vegetables how would we keep the items together, but separate them by their
# fruit/vegetable status?

# One possible solution would be to make 2 lists.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# However the data is somewhat related as they are foods with high pesticide content so this may not be the best way to
# organize it.

# Nested list.
# With this we have nested the list to keep the data together but still separate them based on their fruit/vegetable
# status.
dirty_dozen_2 = [fruits, vegetables]
print(dirty_dozen_2)

# quiz question

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# this is going to list 1 (vegetables) and printing out list item 1 (Kale).
print(dirty_dozen[1][1])