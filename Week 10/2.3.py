try:
    num = int(input("Enter a positive number:"))    # prompting user to input a number
    if num < 0:         # checking if the number is negative
        raise ValueError    # raising error if the number is negative
except ValueError:
    print("Positive numbers only allowed")
