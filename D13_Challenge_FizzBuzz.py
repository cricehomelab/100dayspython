'''
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

Reminder on the rules
numbers divisible by 3 should be "fizz"
numbers divisible by 5 sshould be "buzz"
numbers divisible by both should be "fizzbuzz"

output for the first 25 numbers evaluated
[1]
[2]
FizzBuzz  # should not be printed
Fizz # correct expected response
[3]
[4]
FizzBuzz
Buzz
FizzBuzz
Fizz
[6]
[7]
[8]
FizzBuzz
Fizz
[9]
FizzBuzz
Buzz
[11]
FizzBuzz
Fizz
[12]
[13]
[14]
FizzBuzz
Fizz
Buzz
[16]
[17]
FizzBuzz
Fizz
[18]
[19]
FizzBuzz
Buzz
FizzBuzz
Fizz
[21]
[22]
[23]
FizzBuzz
Fizz
[24]
FizzBuzz
Buzz


# this will get us better results but still not what we want
for number in range(1, 101):
  # changed the "or to an "and" because we need both criteria to be met.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

example of issue
on evalutating 15 we get 3 outputs.
FizzBuzz
Fizz
Buzz

'''

# final fix.

# this will get us better results but still not what we want
for number in range(1, 101):
    # changed the "or" to an "and" because we need both criteria to be met for FizzBuzz.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # this needs to be an elif since we want only one output for each number.
    elif number % 3 == 0:
        print("Fizz")
    # this needs to be an elif since we only want one output for each number.
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Instructor pointed out we don't want the brackets I removed those. 
        print(number)
