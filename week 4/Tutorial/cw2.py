#asking user to input two number

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

#used nested if to check the condition
if num1>0 and num2>0:
    print("The product of the two numbers is:",num1*num2)
else:
    print("The number must be positive")
