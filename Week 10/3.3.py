add = 0
while True:
    try:
        num = input("Enter any number or q to quit:")   # asking user to input a number
        if num == "q":          # condition for user to stop input
            break
        num = int(num)          # converting user input to integer for calculation
        add = add + num         # adding user input
    except ValueError:          # exception handling for invalid input
        print("Invalid Input")

print("The sum is:", add)
