
'''
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even
number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not
every step of the calculation.

Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the
solutions.

'''

#setting up accumulator
sum_of_numbers = 0

# iterating through even number and adding them together.
for number in range(2, 101, 2):
    sum_of_numbers += number

print(sum_of_numbers)


# This is second way i figured out how to solve this. This method was not covered in the solutions provided in the
# course. 
list_of_numbers = []
# this second way adds all the even numbers between 2 and 100 to a list and we use sum() to print the total.

# Create a list of even numbers between 2 and 100.
for number in range (2, 101, 2):
    list_of_numbers.append(number)

print(sum(list_of_numbers))
