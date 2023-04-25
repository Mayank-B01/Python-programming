# defining a function
def extract_temp(letter):
    # splitting each word of in the line
    value = letter.split()
    # using loop to check each word of the line
    for val in value:
        # check if each word is a digit
        if val.isdigit():
            # printing the digit in the line
            print("The number found is:", val)


# asking user inout for file name
sent = input("Enter file name:")
# opening file in read mode
lin = open(sent, "r")
# reading each line of the file
line = lin.read()
print("The lines in the file are:\n", line)
# calling the functions
extract_temp(line)

