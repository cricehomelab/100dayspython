'''

range function is useful for generating a range of numbers to loop through

basic syntax:
for number in range(a, b):
    print(number)



'''

# testing to see if i get the syntax from an explanation alone.

for number in range(1, 10):
    print(number)
# the output of this is ever number from 1 to 9 (this does not include the number 10)
# looks like if we wanted to do the range to include 100 we would have to have the range from 1 to 101.

# This goes back to the early instance of how to print the sum of the first 100 numbers.
# IE. 1 + 2 + 3 +4 + 5 + ........ + 97 + 98 + 99 + 100 = ????

# I solved this before Angela went through this, but when she stepped through this i learned that the variable I called
# sum is called an accumulator.
sum = 0
for number_1 in range(1, 101):
    sum += number_1
print(sum)

# we can specify the number of steps each iteration should go through. In this example it will step up 2 numbers at
# every iteration. IE the first output will be 1, the second will be 3, the third will be 5 and so on.
for number in range(1, 10, 2):
    print(number)

