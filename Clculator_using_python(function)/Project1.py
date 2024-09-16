# Function Definitions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # Check for division by zero
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def modulus(x, y):
    return x % y


# User Input Handling and Calculator Logic
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    # Get user's choice
    choice = input("Enter choice (1/2/3/4/5): ")


    # choice is valid
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input! Please enter a number between 1 and 5.")
        return

    # Get the numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Please enter numeric values.")
        return

    #selected operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):  # If it's an error message
            print(result)
        else:
            print(f"{num1} / {num2} = {result:.2f}")
    elif choice == '5':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")


# Run the calculator program
calculator()
