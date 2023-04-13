# generating random number
import random
r_num = random.randint(1, 20)
# creating a variable to store the inputs of the user as string
ans = ''
for i in range(1, 6):
    # asking user to input a number
    num = int(input("Enter a number:"))
    # condition when user guess correctly
    if num == r_num:
        print("You won in", i, "try")
        print("Congratulation!! You guessed correctly")
        break
    # condition when user guess lower number
    elif num < r_num:
        less = r_num - num
        if less > 5:
            print("Guess was too low")
        else:
            print("Guess is low")
        ans = str(num) + "\t" + ans
    # condition when user guess higher number
    elif num > r_num:
        more = num - r_num
        if more > 5:
            print("Guess is too high")
        else:
            print("Guess is high")
        ans = str(num) + "\t" + ans
    i = i+1
    # adding a condition when the user does not guess right at all chances
    if i == 6:
        print("Your chances are finished! The answer is ", r_num)
        print("Your answers were", ans)

