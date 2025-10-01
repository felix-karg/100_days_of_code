# Calculator

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(previous_result):
    if not previous_result:
        number_1 = float(input("What's the first number? "))
    else:
        number_1 = previous_result
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    number_2 = float(input("What's the next number? "))

    result = operations[operation](number_1, number_2)
    print(f"{number_1} {operation} {number_2} = {result}")
    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continue_calculating == "y":
        calculator(result)
    else:
        calculator(None)

print(logo)

calculator(None)
