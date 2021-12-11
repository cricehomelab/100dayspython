
'''

Nested If/Else statements are if/else statements nested within another if/else statment.

# conceptual example.

# Check to see if the "if" condition is true
if condition:
    # once the fist condition is found to be true the program checks to see if another "if" condition is true.
    if another condition:
        do this
    # If the second condition is false the "else" condition is applied and that is done.
    else:
        do something else
# If the first condition is False then the program will not evaluate the nested statement and will do the other thing
# instead.
else:
    do this other thing

'''

print("Welcome to the RollerCoaster!")
height = int(input("how tall are you in centimeters? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age <= 18:
        print("That will will be $7.00 please.")
    else:
        print("That will be $12.00 please. ")

else:
    print("You are too short to ride.")

'''

If there is further complexity we need to account for like 3 situations you can use an "elif" statement or an elseif


'''

print("Welcome to the RollerCoaster!")
height = int(input("how tall are you in centimeters? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("That will will be $5.00 please.")
    elif age <= 18:
        print("That will be $7.00 please. ")
    else:
        print("That will be $12.00 please.")
else:
    print("You are too short to ride.")