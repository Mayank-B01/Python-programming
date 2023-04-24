# asking user to input two numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
# finding the sum of the two numbers
sum = num1 + num2
# checking if the sum is odd or even
if sum % 2 == 0:
    print("The sum of", num1, "&", num2, "is even")
else:
    print("The sum of", num1, '&', num2, 'is odd')
