# initializing a variable to calculate product
product = 1
# creating loop to take user input and store product of input
while True:
    # prompting user to input a number
    num = int(input("Enter the number: "))
    # using if condition to stop loop when user enters sentinel value 0
    if num != 0:
        # calculating product of user input
        product = product * num
    else:
        # closing loop when user enter 0
        break
print(" The product is", product)