def product(numbers):
    if len(numbers) == 0:       # setting base value for recursion
        return 1
    return numbers[0] * product(numbers[1:])  # multiply first element of the list and calling the function


print("The product is", product([2, 8, 9]))
