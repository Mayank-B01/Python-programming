# asking user to input a string
word = input("Enter any string:")
# creating a variable to count the vowels
count = 0
# creating a loop to count the number of vowels
for char in word:
    if char.lower() == 'a' or char.lower() == "e" or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        count = count + 1
print("The number of vowels in the string is", count)


