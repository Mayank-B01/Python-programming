# creating a function to display the multiplication table
def multiplication(num, power=False):
    # initializing string variables to display data in table form
    line1, line2 = '', ''
    # asking user to input true
    val = input('Enter True/true/t/1: ')
    # setting expo as a boolean variable to check user input
    expo = bool(val == 'True' or val == 'true' or val == 't' or val == '1')
    # checking if power is on
    if expo and not power:
        # creating loop to print header line
        for i in range(1, num + 1):
            line2 = line2 + "\t" + str(i)
        print(line2)
        # creating loop for rows
        for i in range(1, num + 1):
            line1 = str(i) + "\t"
            # creating loop for columns
            for j in range(1, num + 1):
                line1 = line1 + str(i ** j) + "\t"
            print(line1)
    else:
        print("Cannot perform exponentiation")


# Calling the function
multiplication(int(input("Enter a number for grid size: ")))
