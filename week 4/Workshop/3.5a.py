# asking user to input a character
letter = input("Enter A, B or C: ")

# using nested id statement to check the given conditions
if letter == 'A' or letter == "a":
    print("Apple")
else:
    if letter == 'B' or letter == 'b':
        print("Banana")
    else:
        if letter == 'C' or letter == 'c':
            print("Coconut")
        else:
            print("Invalid input")
