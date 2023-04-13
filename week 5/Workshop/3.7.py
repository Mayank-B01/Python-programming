# asking user to input a number
num = int(input("Input a multi-digit number:"))
# creating a variable to store the sum of digits
add = 0
# creating a loop to add digits in the number
for i in range(1, len(str(num))+1):
    remain = num % 10
    add = add + remain
    num = num // 10
print("The sum of the digits is:", add)
