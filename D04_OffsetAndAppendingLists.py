'''

Lists are a form of Data Structure
Data structure - a way of organizing and storing data
Lists are ways to store grouped pieces of data.
Example of a list, a list that stores the names of all the states in the US.

You may also want to keep track of an order for data
If there was a virtual line to do something like buy a PS5 you would want to keep track of who joined first second....
one millionth in line... etc.

example list:
fruits = ["apple", "orange", "banana"]

Lists do not have to keep a consistent data type. IE you can have ints and strings in the same list.

lists have an order to them and as the data is stored the order is not lost.

'''

# List of states in the US in the order that the states joined the Union.
#  Position             0           1               2              3            4               5           6
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# The order of lists start at 0 and count up from that so the first item in the list will be stored at position [0]
# This will print the first item in the list.
print(states_of_america[0])

# prints the 4th item in the list.
print(states_of_america[3])

# You can also count backwards in a list. [-1] will give you the list item in the list.
print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america[-3])

# changing an item in a list
states_of_america[1] = "Pencilvania"
# printing that from the list
print(states_of_america[1])
# Changing it back
states_of_america[1] = "Pennsylvania"
print(states_of_america[1])

# Appending an item to the list.
states_of_america.append("Puerto Rico")

print(states_of_america)
print(states_of_america[-1])

# The extend() function allows you to add multiple items to the list in one go. Example below.
fruits = ["apple", "orange", "pear"]
print(fruits)
fruits.extend(["banana", "peach", "strawberry", "grape"])
print(fruits)

