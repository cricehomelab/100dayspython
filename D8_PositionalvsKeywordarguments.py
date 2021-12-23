
# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"lovely weather we are having in the city of {location}.")

# Call the function while requesting user input.
#                 ARGUMENT1 (name)              ARGUMENT2 (location)
greet_with(input("What is your name? "), input("Where are you today? "))

# calling the function with keyword arguments.
greet_with(location="Georgia", name="Frank")

