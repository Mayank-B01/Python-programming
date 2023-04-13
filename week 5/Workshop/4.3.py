# importing random for generating random number
import random
# initializing variables to count the number of wins and rounds played
count = 0
win_number = 0
# initializing a variable to store answers
answer = ''
# setting loop for generating dice roll and user guess
while True:
    # generating random number for two dice roll and adding them
    dice_roll = random.randint(1, 6) + random.randint(1, 6)
    answer = answer + str(dice_roll) + "\t"
    # asking user to input guess
    your_guess = int(input("Enter your guess:"))
    if your_guess == dice_roll:
        print("You are correct!!")
        win_number = win_number + 1
    else:
        print("You are incorrect!!")
    count = count + 1
    # Asking user if he/she wants to quit
    choice = input("Do you want to quit?")
    if choice.lower() == 'q' or choice.lower() == "yes" or choice.lower() == 'y':
        print("Thank you for playing the game.")
        break
# calculating win percentage
win_per = format((win_number/count)*100, '.2f')
print("the answers were:", answer)
print("The number of rounds played:", count)
print("You win percentage is", win_per, "%")
