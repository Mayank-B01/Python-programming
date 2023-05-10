try:
    num_lst = []        # creating an empty list
    while True:
        num = input("Enter a number or q to quit:")     # prompting user to input numbers
        if num.lower() == 'q':      # checking if user wants to stop adding numbers
            break
        if not num.isdigit():       # checking if user input is valid
            raise TypeError
        num_lst.append(int(num))       # adding user input to the list
    add = 0
    count = len(num_lst)        # counting the length of list
    for number in num_lst:      # accessing the list elements
        add = add + number      # calculating the sum of the elements
    print("The average is:", add/count)
except TypeError:               # checking for invalid input
    print("Only numeric digits allowed")
except ZeroDivisionError:       # checking for no input
    print("No inputs found")
