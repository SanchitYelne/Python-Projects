from art import logo

print(logo)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


x = float(input("Enter the first number : "))
print(" + \n - \n * \n / \n")

do_operation = True
while do_operation:
    operator = input("Enter an operator to perform an operation :")
    y = float(input("What's the next number ? : "))
    if operator == "+":
        result = add(x, y)
    elif operator == "-":
        result = sub(x, y)
    elif operator == "*":
        result = mul(x, y)
    elif operator == "/":
        result = div(x, y)

    print(f"{x} {operator} {y} = {result}")

    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation"
                  f", or type 'e' to exit : ").lower()
    if again == "y":
        x = result
    elif again == "n":
        x = int(input("Enter the first number : "))
        print(" + \n - \n * \n / \n")
    elif again == "e":
        exit()



