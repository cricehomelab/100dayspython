'''

Scope: the idea of what can access certain variables.

'''

enemies = 1


def increase_enemies():
    enemies = 2
    # This print statement will show 2 inside this scope.
    print(f"enemies inside of the function: {enemies}")


increase_enemies()
# This print statement will show 1 as this is a different scope than inside the function.
print(f"enemies outside of the function: {enemies}")

# Local Scope
# this scope exists within functions.

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# If we ran this it will throw an error since we are outside the function and outside the function's scope.
#print(potion_strength)

'''
Here is the error it throws....
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_LocalVsGlobalScope.py", line 30, in <module>
    print(potion_strength)
NameError: name 'potion_strength' is not defined

'''

# Global Scope
# this scope is available within functions.

player_health = 10

def drink_potion_2():
    # This local scope variable potion_strength is available within the function only.
    potion_strength = 2
    # we are able to see our global scope variable player_health from inside of the functions local scope.
    print(player_health)
    print(potion_strength)

    # the lines below do not work due to the scope issue (see Error 2 below for the error).
    # player_health += potion_strength
    # print(player_health)


drink_potion_2()

'''
Error 2 
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_LocalVsGlobalScope.py", line 55, in <module>
    drink_potion_2()
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_LocalVsGlobalScope.py", line 50, in drink_potion_2
    print(player_health)
UnboundLocalError: local variable 'player_health' referenced before assignment
'''

def game():
    def drink_potion_3():
        # This local scope variable potion_strength is available within the function only.
        potion_strength = 2
        # we are able to see our global scope variable player_health from inside of the functions local scope.
        print(player_health)
        print(potion_strength)

    # this works
    drink_potion_3()

# This line will not work See Error 3
# drink_potion3()

'''
Error 3
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_LocalVsGlobalScope.py", line 82, in <module>
    drink_potion3()
NameError: name 'drink_potion3' is not defined
'''

# there is no block scope in Python

# this means a variable defined within an if/for/while can be seen outside of it.
if 3 > 2:
    a_variable = 10

# this will work even though a_variable is defined within the if statement above.
print(a_variable)


game_level_2 = 3
def create_enemy():
    enemies = ["Skelly-boi", "Zomb-boi", "Big-eyed-boi",]
    if game_level_2 < 5:
        new_enemy_2 = enemies[0]
    # Skelly-boi will print out here because it is within the scope of the function.
    print(new_enemy_2)

# Skelly-boi will not print out from this code because we have changed scopes from the create_enemy() function.
# print(new_enemy_2)

'''
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day12Python/D12_LocalVsGlobalScope.py", line 109, in <module>
    print(new_enemy_2)
NameError: name 'new_enemy_2' is not defined
'''



