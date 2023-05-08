month = input("Enter a month:")     # asking user to input a month
for char in month:                  # using loop to check every character in the string
    if char.lower() == "r":         # checking for "r" in the string
        result = "True"
        break
    else:
        result = "False"
print(result)                       # printing the result
