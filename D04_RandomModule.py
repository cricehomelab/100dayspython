'''

Randomization
Computers perform predictable tasks in repeatable ways.
In general many programs, like games, require a degree of unpredictablity.
Python uses a psuedorandom number generator called the Mersenne Twister.

pseudorandom number generators - are random number generators but will eventually repeat, whereas true randomness
does not repeat.

pseudorandom generators take a seed, or a number that is from a true random sequence (you can get this from measuring
noise, or naturally occuring fluctuations) they multiply the seed by itself and take the middle number of the product
and repeat the process.
Eventually pseudorandom generators will repeat, since its not truly random.

The length before a pseudorandom sequence repeats is called a period. The period is limited by the length of the initial
seed.

a two number sequence will repeat after at most 100 repeats of the process

seed * seed = product
 81  *  81  =   8561
 56  *  56  =   3136
 13  *  13  =   and so on until the product becomes 81 again and the pattern repeats.

A 3 digit seed has a max of 1,000 before repeating
a 4 digit seed has a max of  10,000 before repeating

A large enough seed will take trillions of itterations to occur.

The downside of this approach is that there are sequences which can never occur.

big distinction between what is possible and what is possible in a REASONABLE amount of time.

with pseudorandom number generators the security increases as the length of the seed increases.

if we know that it would take the most powerful computer in the world hundreds of years to determine what the random
seed is we can assume the data is practically secure. However, this is not perfectly secure.


'''


# importing a module to get random numbers
import random
# this is a module I created. I have part of the value of pi stored here.
import D04_module

# creates a random number between 1 and 20
print(random.randint(1, 20))

# printing the value of pi i have stored in D4_module module.
print(D4_module.pi)

# creating a random floating point.
print(random.random())

# how to create a random float between 0 and 5
# my attempt.
print(random.random() + random.randint(0, 5))
# instructor method. Probably better.
print(random.random() * 5)

# another way to make a "love score" as we did in a previous days challenge. Because it was pseudoscience.
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
















