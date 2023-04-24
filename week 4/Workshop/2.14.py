# asking user to input a number
num1 = int(input("Enter a number: "))
# assigning another number
num2 = 17
# checking if the input is greater than assigned number and calculating difference
if num1 > num2:
    diff = 2 * abs(num1-num2)
else:
    diff = num2 - num1
print("The difference is ", diff)


