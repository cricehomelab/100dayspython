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


def calculator():
    """Function that runs our calculator."""
    num1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue == True:
        operation_symbol = input("Pick an operation: ")

        calculation_function = operations[operation_symbol]

        num2 = int(input("What is the next number?: "))

        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        if input(f"press 'y' to continue calculating with {first_answer}, 'n' to start a new calculation: ").lower() == 'y':
            num1 = first_answer
        else:
            should_continue = False
            # our function will call itself. Curently this will run infinitely.
            calculator()

calculator()

