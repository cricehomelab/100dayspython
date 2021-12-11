'''

This is a challenge to see if we can detect an even or an odd number. In this challenge we are prompted to use the
modulo or (%) symbol to evaluate the number. The modulo detects the remainder of a number.

If we divide an even number by 2 it will have a remainder of 0
IE 10/2 = 5
If we divide an odd number by 2 it will have a remainder.
IE 9 / 2 = 4.5 (remainder of 5)

If we use the modulo

this determines an even number.
10 % 2 = 0

this determines an odd number.
9 % 2 = 1

'''

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")