try:
    num1 = int(input("Enter first number:"))            # asking for user input
    num2 = int(input("Enter second number:"))
    if num2 == 0:
        raise ZeroDivisionError ("You cannot divide by zero")   # raising zero division error
    else:
        div = num1 / num2                        # performing division
        print("The result for division is:")                # printing result
except Exception as e:
    print("Error:", e)
