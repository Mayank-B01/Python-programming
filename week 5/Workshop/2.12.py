# This program calculates sum of numbers between 1 and 100 that are divisible by 3 and 5
#initializing a value for sum
add = 0
# initializing a variable for loop
i = 1
# creating a loop
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        add = add + i
    else:
        add = add
    i = i + 1
# printing the sum
print("The sum of numbers between 1 and 100 that are divisible by 3 and 5 is", add)
