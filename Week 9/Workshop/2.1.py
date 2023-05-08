
# performing exception handling using try-except statements
try:
    # asking for two user inputs
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    div = num1 / num2
    print("The division of the numbers is:", div)
except ValueError:              # exception for ValueError
    print("You entered wrong value. Integers only allowed.")
except TypeError:               # exception for TypeError
    print("You entered wrong datatype")
except ZeroDivisionError:       # exception for ZeroDivision Error
    print("You can not divide by zero")
except Exception as e:          # global exception case
    print("Error:")
