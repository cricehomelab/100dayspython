# # Play Computer - IE evaluate code line by line and find what the code is doing to give the result that it is.
# Description: when you select 1994 for the year there is no output.

# Broken Code
print("first example start:")
print("Pick 1994 to see the bug.")
year = int(input("What's your year of birth?"))
# PROBLEM: the if/elif statement does not INCLUDE 1994
# 1993 will output millenial
# 1995 will output Gen Z
# 1994 will not output anything because of how the < works.
# need to add >=
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")


# way to evaluate for the year that does not return anything without needing an input (1994)
print("Second example start:")
print("1994 is set to the year in the code rather than by an input")
year = 1994
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Fixed code
print("Third example start:")
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")