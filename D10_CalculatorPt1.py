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
operation_symbol = input("Pick an operation from the lines above:")
num2 = int(input("What is the second number?: "))

for symbol in operations:
    print(symbol)

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


