##CalculatorProject

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
functions={"+": add,"-": subtract,"*": multiply,"/": divide,}

def calculator():
    continue_calculation=True
    n1 = float(input("What is the first number?: "))

    while continue_calculation:
        for symbol in functions:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        result = functions[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = result
        else:
            continue_calculation= False
            #print("\n" * 20)
            calculator()


calculator()
