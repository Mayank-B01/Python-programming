# This program adds all the positive integers entered by the user
# assigning a boolean value to start a loop
condition = True
# initializing a variable to sum positive integers
add = 0
# starting a loop to add positive numbers
while condition == True:
    num = int(input("Enter any number:"))
    if num > 0:
        if num > 100:
            break
        else:
            add = add + num
            # asking user choice whether he wants to continue or not
            cont = input("Do you want to continue(y/n)?")
            if cont.lower() == 'y' or cont.lower() == 'yes':
                continue
            else:
                break
                condition = False
    else:
        print("please enter again")
print("The sum of positive numbers entered by the use is", add)

