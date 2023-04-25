colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Open a file in write mode
file = open('colors.txt', 'w')
# Write each color in the list to a new line in the file
for color in colors:
    file.write(color + " \n")
file.close()
print("Colors written to file successfully.")
with open('colors.txt', 'r') as files:
    print(files.read())
