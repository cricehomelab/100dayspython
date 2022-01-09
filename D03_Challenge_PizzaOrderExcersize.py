'''

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

'''

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bill = 0

# need to check what size pizza they want so we can add the right amount to the bill.
# check size to see if its small
if size == "S":
    bill += 15
# check size to see if its medium
elif size == "M":
    bill += 20
# if it is not small or medium it must be large.
else:
    bill += 25

# adding extra cheese costs $1 no matter what.
if extra_cheese == "Y":
    bill +=1

# Check to see if they want extra pepperoni
if add_pepperoni == "Y":
    # adding pepperoni is more expensive for medium or large pizza compared to a small.
    if size == "S":
        # adding pepperoni costs $2
        bill += 2
    else:
        # if they want the extra pepperoni and the size isn't small it must be medium or large
        # so we need to add $3 to the bill.
        bill += 3
# Since this won't change the bill further we cam print the amount due out

print(f"Your final bill is: ${bill}.")

