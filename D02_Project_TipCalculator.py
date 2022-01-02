'''
Requirements:
Take an input of the check.
Ask for a tip percentage.
Ask for how many people are splitting the bill.
determine how much each person should pay.

Some math needed in this:
bill = (check_total + tip)
bill = (check_total + (check_total * tip_percent)

portion = Bill / Diners

portion = (check_total + (check_total * tip_percent)) / diners

need to see 2 decimals of precision
'''

print("Welcome to the tip calculator. ")
check_total = float(input("How much is the total check? $"))
tip_percent = int(input("What percent do you want to tip (ex. 10, 12, 15)? ")) / 100
diners = int(input("How many people are splitting the bill? "))
portion = "{:.2f}".format((check_total + (check_total * tip_percent)) / diners)
print(f"Each person should pay ${portion}.")




