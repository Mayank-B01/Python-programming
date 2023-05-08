import random       # importing random module to generate random number
try:                # using try-except block for error handling
    random_num = random.randint(1,10)       # generating random number
    guess = int(input("Enter your guess"))  # asking user input for guess
    if guess == random_num:                 # comparing guess and random number
        print("You are correct! ")
    elif guess > 10:                        # case for when user input is out of range
        raise Exception
    else:
        print("You are incorrect! The answer is:", random_num)
except ValueError:                         # case for invalid value input
    print("You have entered invalid value.")
except Exception:
    print("Value is out of range")


