# asking user to input a number
num = int(input("Enter a number:"))
# initializing the factorial value
fac = 1
# assigning a variable to store the input number
val = num
# using loop to calculate the factorial
while num != 0:
    fac = fac * num
    num = num - 1
print("The factorial of ", val, "is", fac)
