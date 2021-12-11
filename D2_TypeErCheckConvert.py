
num_char = len(input("What is your Name? "))
'''
the follwoing example will not work because the output of a len() function is an integer, and we cannot
concatonate a string with an integer. 

print("Your name has " + num_char +  " characters in it.")

Error: 
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day2Python/venv/TypeErCheckConvert.py", line 3, in <module>
    print("Your name has " + num_char +  " characters in it.")
TypeError: can only concatenate str (not "int") to str

'''
# In order to get this to print out we need to make sure all the data type match so we need to convert the integer to a
# string.

# the type function will tell us what kind of data is stored in a variable.
print(type(num_char))
# In this case it will output <class 'int'> to tell us it is an integer.

# We can use the str() function to take the integer and make it into a string for the purpose of writing out
# our sentence.
print("your name has " + str(num_char) + " characters in it.")

# Here are other examples of converting data types.
a = 123
print(a)
print(type(a))
b = str(a)
print(b)
print(type(b))
c = float(a)
print(c)
print(type(c))

# this will add the numbers together and will output 170.5
print(70 + float(100.5))

# this will print out 70100.5 as this concatonates rather than adding the 2 numbers.
print(str(70) + str(100))


