month = input("Enter a month:")     # asking user to input a month
count = 0                           # initializing a counting variable
for char in month:                  # using loop to check every character in the string
    if char.lower() == "r":         # checking for "r" in the string
        count = count + 1           # counting the number of times 'r' appears
    else:
        count = count
print("The letter 'r' was repeated", count, "times")           # printing the result
