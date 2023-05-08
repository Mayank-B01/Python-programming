# using try-except block for exception handling
try:
    lst = []        # creating an empty list
    while True:     # using while loop to take multiple user input
        num = int(input("Enter any number:"))
        lst.append(num)         # adding user input to list
        choice = input("Press y or yes to continue or any keys to quit:")
        if choice.lower() == "y" or choice.lower() == "yes":    # condition for adding more user input
            continue
        else:
            break
    print(lst)
    add = 0         # initializing the variable for sum of the numbers
    for i in lst:
        add = add + i
    total = len(lst)
    print(total)
    average = add / total       # calculating the average
    print("The average is:", average)
except (ValueError, TypeError):     # exception handling
    print("You have entered non-numeric value")

    