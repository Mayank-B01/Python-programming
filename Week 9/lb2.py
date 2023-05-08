try:
    # Generate a ZeroDivisionError
    a = 10
    b = 0
    div = a / b
    print(div)
except:
    print("ZeroDivisionError: Cannot divide by zero")

try:
    # Generate a ValueError
    import math
    y = math.sqrt(-6)
except:
    print("ValueError: Invalid literal for int() with base 10: 'abc'")

try:
    # Generate a NameError
    print(add)
except Exception as e:
    print("Error: ",e)
