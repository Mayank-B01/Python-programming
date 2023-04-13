# This program uses loop to add even number between 100 and 200 inclusive
# initializing a variable to define start value of loop
num = 100
# initializing a variable to store sum of numbers
add = 0
# creating a loop to add even number between 100 and 200
while num <= 200:
    if num % 2 == 0:
        add = add + num
    num = num + 1
print("The sum of even numbers between 100 and 200 is", add)
