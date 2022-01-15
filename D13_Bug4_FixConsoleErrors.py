# # Fix the Errors
# commented out because it will not run.
#age = input("How old are you?")
#if age > 18:
#print("You can drive at age {age}.")

'''
Running this code unchanged gives this error in the console

  File "C:/Users/charl/PycharmProjects/Day13Python/D13_Bug4_FixConsoleErrors.py", line 4
    print("You can drive at age {age}.")
    ^
IndentationError: expected an indented block

It also underlines the "p" in print.

If you mouse over that error it will say "Indent Expected"

'''

# fixed code part 1
# Will error out again. So commented out.
#age = input("How old are you?")
#if age > 18:
#    print("You can drive at age {age}.")

# If you run the code above it will also error out with this error:

'''
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day13Python/D13_Bug4_FixConsoleErrors.py", line 23, in <module>
    if age > 18:
TypeError: '>' not supported between instances of 'str' and 'int'

'''

# Fixing that error to allow for the number to be evaluated as an integer.
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")

# the code above outputs "You can drive at age {age}."
# final fix

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")


