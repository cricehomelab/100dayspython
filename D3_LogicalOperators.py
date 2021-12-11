'''

Logical operators - checking multiple conditions in the same line of code

if condition1 & condition2 & condition3:
    do this
else:
    do this instead

3 different logical operators

A and B     when you combine 2 different conditions with "and" they BOTH must be true.
C or D      when you combine different conditions with "or" only ONE of the conditions must be true.
not E

from the console:

# using "and" to join conditions.
a = 12
# checking to see if a is greater than 14
a > 14
# this returns False

False
# checking to see if a > 10
a > 10
# This returns True

True
# checking to see if a is greater than 10 AND if a is greater than 13
a > 10 and a < 13
# because a equals 12 it is both greater than 10 and less than 13 both statements are true and True is returned

True
# if we check to see if a is greater than 15 and if a is less than 13 only one of those are true making the return be
# False.
a > 15 and a < 13

False

# using "or" to join conditions.
# "or is used if you are evaluating multiple statements and you only need one of the conditions to be true in order
# to proceed.

# using the "not" operator reverses a condition.
# if a condition is True it becomes False.
# if a condition is False it becomes True.

a = 12
# we know that a is 12 and that is less than 5 not greater than 15. The statement below will evaluate to True because
# because if we evaluate a > 15 we would get False, but since we are looking at not a > 15 we will get True. d
not a > 15


'''

# The following is a futher iteration on our "rollercoaster ticket booth" example that we have been working on in day 3
# In this case we are giving free tickets to people who are having a midlife crisis.
# For the sake of this example we are assuming people between 45 and 55 are having a midlife crisis based on the likely
# age that this occurs (Based on Wikipedia).
# This is my attempt at it which was slightly different from the instructor example.

print("Welcome to the RollerCoaster!")
height = int(input("how tall are you in centimeters? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("child tickets are $5.00.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.00. ")
        bill += 7
    elif age > 18:
        # This is where i added my 
        if age <=55 and age >=45:
            # midlife crisis
            print("This one is on us. Your ticket is free. ")
        else:
            print("Adult tickets are $12.00.")
            bill += 12
    want_photo = input("Do you want a photo taken? Y or N. ")
    # i want the input to be capital regardless i googled how to do this and found:
    # https://www.geeksforgeeks.org/string-capitalize-python/
    if want_photo.capitalize() == "Y":
        bill += 3
    print(f"Your total bill is ${bill}")

else:
    print("You are too short to ride.")

'''
# This is the instructor example they added an extra elif to the main if/elif/else tree. 

print("Welcome to the RollerCoaster!")
height = int(input("how tall are you in centimeters? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("child tickets are $5.00.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.00. ")
        bill = 7
    # This is where the instructor added their extra condition. 
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12.00.")
        bill = 12
    want_photo = input("Do you want a photo taken? Y or N. ")
    # i want the input to be capital regardless i googled how to do this and found:
    # https://www.geeksforgeeks.org/string-capitalize-python/
    if want_photo.capitalize() == "Y":
        bill += 3
    print(f"Your total bill is ${bill}")

else:
    print("You are too short to ride.")

'''