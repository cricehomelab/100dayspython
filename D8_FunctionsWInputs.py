# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("This is my greeting")
    print("It is a function")

greet()

# allowing the function to accept input.
#          name is an PARAMETER
def greet2(name):
    print(f"Hello {name}")
    print("This is my greeting")
    print("It is a function")

#      The input statement here is the ARGUMENT
greet2(input("What is your name? "))

# calling the function with a static thing.
#      "Frank" is an ARGUMENT
greet2("Frank")

# function can also be called with a variable
names = "jeff"
#      names is an ARGUMENT
greet2(names)