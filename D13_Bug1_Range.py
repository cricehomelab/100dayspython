# # Describe Problem
# Description: should print out "You got it" when i = 20, but nothing ever prints.
# Problem: range does not include the highest number in the range.

def my_function():
   for i in range(1, 20):
     # helps to visualize if i ever reaches 20.
     # print(i)
     if i == 20:
       print("You got it")
my_function()

# Solution increase the range to 21.
def my_function_fixed():
   for i in range(1, 21):
     if i == 20:
       print("You got it")
my_function_fixed()