
# review of yesterday
# this will output the number of characters in the word "Hello" or wil output 5
print(len("Hello"))

# This sort of action will not work with printing out different data types like an integer
'''
Trying to run code like this line below:

print(len(13232))

Will output an error like this. I've commented it out and copied the error. 

Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day2Python/venv/primtivedatatypes.py", line 8, in <module>
    print(len(13232))
TypeError: object of type 'int' has no len()

'''
# String
example_string = "Hello"
# you can print specific elements from a string this is called SUBSCRIPT
print(example_string[0])
print(example_string[1])
print(example_string[2])
print(example_string[3])
print(example_string[4])

# you can make a number a string if it stays in between quotes
print("123" + "456")
# the output here is concatenated not added together.
# you can also print out the length of a number like this since it has been made a string.
print(len("123456"))

# Integer
# common exepression for a whole number (number with no decimal place)
integer_example_1 = 123
integer_example_2 = 456
# we can add these numbers together and they  will add up to the sum of 123 + 345 (or 579)
integer_example_3 = integer_example_1 + integer_example_2
# way to print out an integer as a string by wrapping the integer in the str() function.
print(str(integer_example_1) + " + " + str(integer_example_2) + " = " + str(integer_example_3))

# the follwoing is interpreted as 123,456,789 this allows for much more readable numbers in the code.
# The "_" is interpreted as what we would understand a "," to be.
integer_example_4 = 123_456_789
print(integer_example_4)

# Float
# short for a floating point number
pi_is = 3.14159

# Boolean
# this is a True or False value.

boolean_True = True
boolean_False = False
# This is not a boolean it is a string since it is in quotes.
not_a_Boolean = "True"
