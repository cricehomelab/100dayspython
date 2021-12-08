
'''
 Solution 1
 This uses 2 new variables to swap the values. 
'''

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Store a and b in 2 different variables.
c = a
d = b

# switch the values of a and b

a = d
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

'''
 Solution 2
 This is with one less variable declared.
'''

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Store a in a different container.
c = a
# set a equal to b.
a = b
# set b equal to the original value of a.
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
