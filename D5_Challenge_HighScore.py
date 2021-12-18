
'''
Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91

My approach.
1. create for loop to go through the list.
2. check against a variable called high_score
3. if a number is higher then the number in high score replace high_score's value with that number
4. print the high score at the end.
'''

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# my solution that works

# declaring a variable to hold the high score
high_score = 0
# Iterating through the student_scores list
for score in student_scores:
    # comparing the score in the list to the high_score value
    if score > high_score:
        # if the score is higher than the current value of high_score replace the high_score value.
        high_score = score

# printing out the results.
print("The highest score in the class is: " + str(high_score))

# cheating way with the max() function.
print("The highest score in the class is: " + str(max(student_scores)))

# this is how you could print the lowest score with the min function.
print("The lowest score in the class is: " + str(min(student_scores)))
