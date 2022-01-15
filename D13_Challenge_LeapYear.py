'''
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

error output on run:
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day13Python/D13_Challenge_LeapYear.py", line 3, in <module>
    if year % 4 == 0:
TypeError: not all arguments converted during string formatting


'''

# error in the above code was that we need to make the year variable an int. 
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")