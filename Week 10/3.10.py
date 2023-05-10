def gcd(num1, num2):        # defining a function to calculate the greatest common denominator
    if int(num2) == 0:           # setting the base value
        return int(num1)
    return gcd(int(num2), int(num1) % int(num2))   # calculating the gcd using recursive function


def number(number1, number2):               # defining a function to check user input
    while True:
        try:
            if not(number1.isdigit()) and not(number2.isdigit()):       # checking for invalid input4
                raise ValueError    # raising exception
            return num1, num2       # returning number if no exception
        except ValueError:
            print("Positive number only allowed")


num1 = (input("Enter a number:"))       # asking user input
num2 = (input("Enter another number:"))
number(num1, num2)          # calling function for valid input
print("The greatest common denominator is:", gcd(num1, num2))    # calling function for calculation gcd
