# creating a sample list
numbers = [11, 22, 33]
# creating an empty variable to store the single integer
single_int = ''
# joining the multiple integers by converting into string
for num in numbers:
    single_int = single_int + str(num)

# printing the original list
print("The list is:", numbers)
# printing the single integer
print("The single integer for the list is", int(single_int))

