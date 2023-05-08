try:
    num1 = int(input("Enter first number:"))            # asking for user input
    num2 = int(input("Enter second number:"))
    div = num1 / num2                                   # performing division
    print("The result for division is:")                # printing result
except ZeroDivisionError:                               # exception handling for zero division error
    print("You cannot divide by zero.")
