
'''

if / elif / else

if condition1:
    do A
elif condition2:
    do B
else:
    do C

multiple if

if condition1:
    do A
if condition2:
    do B
if condition3:
    do C

The following example that was worked on during the video is a further iteration on the "roller coaster ticket booth"
that has been worked on through day 3's examples. 
'''



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