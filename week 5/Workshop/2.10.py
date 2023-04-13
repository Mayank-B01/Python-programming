# initializing a counting variable
counter = 1
# initializing a number for multiplication
num = 1
product = 1
# Creating a loop to multiply first 20 numbers divisible by 5
while counter <= 20:
    if num % 5 == 0:
        product = product * num
        counter = counter + 1
        num = num + 1
    else:
        num = num + 1
print("The product of first 20 numbers divisible by 5 is", product)
