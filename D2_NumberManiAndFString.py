# this prints out as "2.6666666666666665"
print(8/3)
# this will just output "2"
print(int(8 / 3))
# this rounds the number up to "3"
print(round(8 / 3))
# you can use round to specify precision of the rounding that you want to do
# output 2.67
print(round(8/3, 2))
# output 2.667
print(round(8/3, 3))
# output 2.6667
print(round(8/3, 4))

# This will remove the decimal and will not follow rounding rules without converting to an integer.
# The output here will just be 2.
print(8 // 3)

# result is declared as 4 / 2 so this will equal 2
result = 4 / 2
# the value of result is again divided by 2 to make result = 1
result /= 2
print(result)
# variable declared and assigned a value of 0
score = 0
# the variable now equals itself (0) and adds 1 to that value so score = 1
score += 1
print(score)
# similar to the += this will make the value of score (currently 1) equal itself minus 1.
score -= 1
# This also applies for "variable *= n" where variable is equal to itself multiplied by n which is a number.


# F-strings and using them
value_test = 100
float_test = 1.56
bool_test = True

# adding the f to the 
print(f"integer {score}, float {float_test}, and boolean value {bool_test}")
