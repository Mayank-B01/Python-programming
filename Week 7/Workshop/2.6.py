def count(line):       # defining a function to count the character
    counter = 0         # initializing a counter to count the characters
    for char in line:  # using loop to check each character
        if char != " " or char != "/n":     # not including space and new line character
            counter = counter + 1           # counting the character
        else:
            counter = counter
    return counter          # returning the count


f_name = input("Enter a file name:")        # asking the user to input file name
with open(f_name, "r") as file:             # opening the file in read mode
    lines = file.read()

print("The lines are:", lines)      # printing the line in the file
print("The number of characters are:", count(lines))       # printing the number of characters
