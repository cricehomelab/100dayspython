
'''

The idea of this challenge it to "hide" a treasure chest on a grid.

Board layout
Grid layout
        1  2  3   column
  1    [ ][ ][ ]
  2    [ ][ ][ ]
  3    [ ][ ][ ]
rows

The input will be a 2 digit number that specifies the column then the row.
From the input the program will place an x in that position.

example input 23

Where the 'X' should be placed.
        1  2  3   column
  1    [ ][ ][ ]
  2    [ ][ ][ ]
  3    [ ][X][ ]
rows

'''


# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# converting the rows the player knows to the correct index positions.
position2 = int(position[0]) - 1
position1 = int(position[1]) - 1

# Replacing the "⬜️" with "X"
map[position1][position2] = 'X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


