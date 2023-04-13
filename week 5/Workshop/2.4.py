# asking user to input a number
num = int(input("Enter a number"))
while num < 0:
    print("You entered negative number. Try again!")
    num = int(input("Enter a number"))
# using loop for multiplication table
for i in range(1,11):
    # printing the multiplication table
    print(num, "*", i, '=', num*i)

