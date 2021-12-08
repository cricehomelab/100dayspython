'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

the goal here is to solely output the number that is the sum of the 2 digit number. The example output listed

3 + 9 = 12
12

as the expected output but based on the tests it looks like the output they would expect if someone entered '39' as an
example would just be

12

'''


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Method 1

a = int(two_digit_number[0])
b = int(two_digit_number[1])
c = a + b

print(c)

# Method 2.
print(int(two_digit_number[0]) + int(two_digit_number[1]))