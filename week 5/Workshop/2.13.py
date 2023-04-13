# This program calculates sum of numbers between 1 and 100 that are not divisible by 3 or 5
# initializing a value for sum
add = 0
# initializing a variable for loop
i = 1
# creating a loop
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        add = add
    else:
        add = add + i
    i = i + 1
# printing the sum
print("The sum of numbers between 1 and 100 that are not divisible by 3 or 5 is", add)

