# importing random for generating random number
import random
# setting loop for generating dice roll and user guess
while True:
    # generating random number for two dice roll and adding them
    dice_roll = random.randint(1, 6)+ random.randint(1, 6)
    # asking user to input guess
    your_guess = int(input("Enter your guess:"))
    if your_guess == dice_roll:
        print("You are correct!!")
    else:
        print("You are incorrect!!")
    # Asking user if he/she wants to quit
    choice = input("Do you want to quit?")
    if choice.lower() == 'q' or choice.lower() == "yes" or choice.lower() == 'y':
        print("Thank you for playing the game.")
        break
