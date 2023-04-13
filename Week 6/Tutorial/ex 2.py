# creating a list
digits = [54, 67, 63, 2,7]
# creating a variable to store largest number
highest = 0
# creating a loop to find the highest number in the list
for num in range(len(digits)):
    if digits[num] > highest:
        highest = digits[num]
print("The largest number in the list is:", highest)
