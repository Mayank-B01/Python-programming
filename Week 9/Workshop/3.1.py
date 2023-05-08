import math             # importing math module
try:
    num = input("Enter a number:")      # asking user input as string
    number = int(num)                   # converting string to integer
    result = math.sqrt(number)          # calculating square root
    print(result)
except ValueError:                      # exception handling for value error
    print("You can only enter number")
    