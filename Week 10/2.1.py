def natural_sum(num):       # defining a function to perform recursion
    if num == 0:            # defining the base value
        return 0
    else:
        return num + natural_sum(num-1)     # adding the numbers using recursion


number = int(input("Enter any number:"))
print("The sum of first", number, "natural numbers:", natural_sum(number))


