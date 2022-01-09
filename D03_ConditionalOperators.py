
'''

if/else statements are conditional statements where "if" a condition is met something will happen and if it is not met
or "else" it will do something different.

example of what an if/else statement may look like.
if condition:
    do this
else:
    do this

'''

# example of an if/else statement where the else condition is met.
water_level = 50
if water_level > 80:
    print("drain water.")
else:
    print("Continue...")

# Example of an if/else statement where the if condition is met.
water_level = 90
if water_level > 80:
    print("drain water.")
else:
    print("Continue...")


# Example 1 of an if statement
print("Welcome to the RollerCoaster!")
height = int(input("how tall are you in centimeters? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("You are too short to ride.")

'''

Operator        Meaning
>               Greater than
<               Less than
>=              Greater than or equal to
<=              Less than or equal to
==              Equal to
!=              Not equal to

'''

# Example 2 of an if statement.
pick = int(input("Pick a number between 0 and 10. "))
num = 7
if pick == num:
    print(f"you guessed the number correctly ({num} is a cool number!)")
else:
    print(f"You lose the number was {num}.")

