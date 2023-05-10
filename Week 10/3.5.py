def factorial(num):             # defining a recursive function
    if num == 1:                # defining base value to stop the function
        return 1
    return num * factorial(num - 1)     # calculating factorial by calling the recursive function


try:
    number = int(input("Enter any number:"))    # asking for user input
    print("The factorial is :", factorial(number))      # printing the answer
except Exception as e:      # exception handling for wrong input
    print("Error:", e)
