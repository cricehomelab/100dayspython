

enemies = "Skelly-boi"

def increase_enemies():
    # this is not the same variable as the enemies outside the function.
    enemies = "Zomb-boi"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# if we want to modify a global variable from inside a function

enemies_fixed = 1
print()
print("After declaring the global variable in the function. ")
print("This method is not ideal...")
# It's not ideal because this variable could be created anywhere in the code, and it could be unintentionally modifying
# something we do not want to.
def increase_enemies_2():

    # this doesn't work see error 1
    # enemies_fixed += 1

    # to modify a global variable from within a function you have to explicitly call the variable in the
    # function.
    global enemies_fixed
    # now this will work.
    enemies_fixed +=1

    print(f"enemies inside function: {enemies}")


increase_enemies_2()
print(f"enemies outside function: {enemies}")

'''

error 1
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_ModifyGlobalVariables.py", line 24, in <module>
    increase_enemies()
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_ModifyGlobalVariables.py", line 20, in increase_enemies
    enemies_fixed += 2
UnboundLocalError: local variable 'enemies_fixed' referenced before assignment

'''

# Since it is not ideal and highly discouraged to modify global variables within the scope of a function.
# Here is how you would be able to modify them in a more appropriate way.

print("\n a more proper way to change a global variable from a scope. \n")
enemies_3 = 1
def increase_enemies_3():
    return enemies_3 +1

enemies_3 += increase_enemies_3()
print(f"enemies outside function: {enemies_3}")
