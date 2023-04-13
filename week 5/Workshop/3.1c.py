# initializing variable for start value and sum
add = 0
start_value = 100

while True:
    # checking if the number is even
    if start_value % 2 == 0:
        # adding numbers when the number is even
        add = add + start_value
        start_value = start_value + 1
    elif start_value > 200:
        # breaking the loop when the number exceed 200
        break
    else:
        # increasing value of numbers
        start_value = start_value + 1
        continue

print("The sum of even numbers between 100 and 200 is", add)
