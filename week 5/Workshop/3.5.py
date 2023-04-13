# asking user to input a number
number = int(input("Enter a number: "))
# creating a variable to store the main input number
num = number
# initializing a variable with maximum digit known to compare with user input digits
min_val = 9
# creating a loop to compare the digits
while number > 0:
    val = number % 10
    if val < min_val:
        min_val = val
    # using integer division to remove the last digit
    number = number // 10

print("The smallest digit in", num, "is", min_val)
