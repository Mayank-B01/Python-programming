def calculate(equation):        # defining a function to perform calculation
    operation = equation.strip()
    items = operation.split(" ")
    num1 = float(items[0])     # changing the type to int for calculation
    operator = items[1]
    num2 = float(items[2])     # changing the type to int for calculation
    if operator == '+':
        print(operation, "=", num1 + num2)
    elif operator == '-':
        print(operation, '=', num1 - num2)
    elif operator == '*':
        print(operation, '=', num1 * num2)
    elif operator == '/':
        print(operation, '=', num1 / num2)
    else:
        print(operation, '=', float(eval(operation)))


with open("equation.txt", "r") as file:     # reading the file
    for line in file:
        calculate(line)
