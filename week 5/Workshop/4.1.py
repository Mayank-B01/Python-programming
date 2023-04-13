# defining a function that takes two user input and performs calculation of user choice
def calculator():
    # taking two user input
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    # taking input to perform calculation
    y_choice = input("Enter your choice of calculation (a/s/d/m):")
    if y_choice == 'a' or y_choice == 'A':
        add = num1 + num2
        print("The sum of th two numbers is ")
        return add
    elif y_choice == 's' or y_choice == 'S':
        diff = num1 - num2
        print("The difference of the two numbers is")
        return diff
    elif y_choice == 'd' or y_choice == 'D':
        div = num1 / num2
        f_div = format(div, '.2f')
        print("The division of the two numbers is")
        return f_div
    elif y_choice == 'm' or y_choice == 'M':
        mul = num1 * num2
        print("The product of the two numbers is")
        return mul
    else:
        print("Wrong input! Try again")


# Creating a loop to call function for user to input number
while True:
    # calling the function
    operation = calculator()
    print(operation)
    # asking user if he wants to quit
    choice = input("Press q to quit or any other button to continue: ")
    if choice == 'q' or choice == "Q" or choice == "quit" or choice == 'Quit':
        print("Thank you for using the calculator!!")
        break
    else:
        continue
