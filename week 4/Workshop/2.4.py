#asking a user to input age
age=int(input("Enter you age"))

#checking if the person can vote
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")