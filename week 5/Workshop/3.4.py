# asking user to input the number in string format
number = input("Enter a number: ")
# initializing a variable to store highest digit
high_value = 0
# creating a loop to compare digits
for value in number:
    # converting the looping variable to integer for comparison
    if int(value) > high_value:
        high_value = int(value)
# printing the highest digit
print("The largest digit in", number, "is", high_value)
