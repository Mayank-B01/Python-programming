# Initializing counting variables for input
pos_num = 0
neg_num = 0
zero_num = 0
condition = True
# creating a loop for user input
while True:
    if condition == True:
        # asking user to input a number
        num = int(input("Enter a number"))
        if num < 0:
            neg_num = neg_num + 1
        elif num > 0:
            pos_num = pos_num + 1
        else:
            zero_num = zero_num + 1
    else:
        break
    # creating a loop to ask user if he/she wants to continue
    while condition == True:
        choice = {'N', 'n', 'no', 'NO'}
        user_choice = input("Do you want to continue?(Y/N)")
        if user_choice in choice:
            condition = False
            break
        elif user_choice == "y" or user_choice == 'Y' or user_choice == 'yes' or user_choice == "YES":
            break
        else:
            print("Wrong input! Try again")
            user_choice = input("Enter again")
            break

print("The count of positive number input is:", pos_num)
print("The count of negative number input is:", neg_num)
print("The count of zero input is:", zero_num)
