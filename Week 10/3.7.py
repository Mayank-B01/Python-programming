def factorial(num):     # defining a recursive function for calculating factorial
    if num == 1:        # setting base value
        return 1
    return num * factorial(num - 1)     # calculating factorial by calling the function


try:
    number = int(input("Enter any number:"))        # asking for user input
    print("The factorial is :", factorial(number))  # calling the function
except Exception as e:              # exception handling for invalid input
    print("Error:", e)
