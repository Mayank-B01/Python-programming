# keep in loop until user enter zero
number = int(input("Enter a number"))
add = 0
# checking user input
while number != 0 :
    print("You have not entered zero. Try again")
    add = add + number
    number = int(input("Enter number again: "))

print("You have finally entered zero! Thank You")
print("The sum is ", add)

