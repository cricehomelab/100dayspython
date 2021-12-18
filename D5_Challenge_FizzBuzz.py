'''

Prompt
Submissions/Test Runs (0)
Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

Hint
1. Remember your answer should start from 1 and go up to and including 100.
2. Each number/text should be printed on a separate line.


'''

'''
Method 1:
This seems to be a lot more hard coded to me. 
'''

# creating a for loop with the desired range of 1 stopping after the number 100 has been tested.
for number in range(1, 101):
    # checking to see if the number is divisible by 3 but not divisible by 5.
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    # checking to see if the number is divisible by 5 but not divisible by 3.
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    # checking to see if the number is divisibly by both 5 and 3.
    elif number % 5 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # else statement to print the number.
    else:
        print(number)

'''
Not sure if im right or not here but this one feels a little more elegant to me. 
'''

# creating a for loop with the desired range of 1 stopping after the number 100 has been tested.
for number in range(1, 101):
    # The statement variable will reset to "" each time through the loop.
    statement = ""
    # check to see if the number is divisible by 3 and add "Fizz" to my statement variable if it is.
    if number % 3 == 0:
        statement += "Fizz"
    # check to see if the number is divisible by 5 and add "Buzz" to my statement variable if it is.
    if number % 5 == 0:
        statement += "Buzz"
    # check to see if the number is not divisible by 3 or 5 and add the number to my statement if it is.
    if number % 3 != 0 and number %5 != 0:
        statement = str(number)
    print(statement)

'''
Just after running through this 2 times i think there are a lot of ways to solve this question. These are just the 
first 2 methods I came up with. 

Here is the instructor solution which was a little different then both of my solutions. 
'''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)