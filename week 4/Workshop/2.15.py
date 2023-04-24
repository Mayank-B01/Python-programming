# asking the user to input two number
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
# adding the two numbers
add = num1+num2
# checking the given condition
if 15 < add < 20:
    add = 20
    print("The sum is ", add)
else:
    print("the sum is ", add)
