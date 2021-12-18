
'''

Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187

Example Output
171

Hint
Remember to use the round() function to round the average height before you print it.

'''


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# An average is the sum of a set of numbers divided by the number of numbers that were added together

#     sum of all observations
#  ------------------------------  = the average
#   Total # of all observations

# this variable will hold the sum of all observation
total_height = 0
# this variable will hold the total number of observations
students = 0

# I did this in one for loop instead of 2 as shown in the solution.
# for each item in the list it first takes that number and adds it to the sum of the total_height variable.
# Second, it adds 1 to the total number of students.
for student in student_heights:
  total_height += student
  students +=1

# This variable calculates the average height, although we could print this average without making a variable if we
# wanted to.
average_height = total_height / students
# Printing this with a variable.
print(round(average_height))
# Printing this without a variable.
print(round(total_height / students))

# easy way that's not allowed.
# this is the same way to do this without a for loop.

# how to save this to a variable.
average_height_cheat = round(sum(student_heights) / len(student_heights))
# how to print this out without a variable.
print(round(sum(student_heights) / len(student_heights)))

# Quick explanation of the above code.
# sum() this function takes the items in a list and adds them all together.
# len() this function takes the items in a list and counts how many there are.
