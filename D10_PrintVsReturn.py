# calculator



def add(n1, n2):
    """add(n1, n2) adds n1 and n2 and returns the sum. """
    return n1 + n2

def subtract(n1, n2):
    """subtract(n1, n2) takes n1 and subtracts n2 and returns the result. """
    return n1 - n2

def multiply(n1, n2):
    """multiply(n1, n2) takes n1 and n2 and multplies them returns the product of the multiplication. """
    return n1 * n2

def divide(n1, n2):
    """divide(n1, n2) returns the result of n1 / n2. """
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
            }

num1 = int(input("What is the first number?: "))
for symbol in operations:
    print(symbol)

# the next 2 lines need to run in sequence if we are doing subsequent equations without a loop
operation_symbol = input("Pick an operation from the lines above: ")
calculation_function = operations[operation_symbol]

num2 = int(input("What is the second number?: "))

first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# long story short return is better because it can be used more ways than print can.

# again, the next 2 line need to run before the calculation is completed.
# if not done this way the operator from the first equation will not change.
operation_symbol = input("pick another operation: ")
calculation_function = operations[operation_symbol]

num3 = int(input("Pick another number: "))
# an example of why return is better
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# this is a good example of why its better to loop to remove the possiblity of simple, but stupid mistakes. 