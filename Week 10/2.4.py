file_name = input("Enter the file name:")   # prompting user to input file name
with open(file_name, "r") as file:      # opening file in read mode
    lines = file.read()             # reading the contents of the file

print("The lines in the files are:\n", lines)   # printing the contents of the original file
old_word = input("Which word do you want to replace?:")     # asking for the word to be replaced
new_word = input("Which word do you want ro insert?:")      # asking for the word to insert

new_lines = lines.replace(old_word, new_word)       # replacing the words
print("The new lines are:\n", new_lines)            # printing the line after replacing the words
