file_name = input("Enter the file name:")       # prompting the user to input file name
with open(file_name, "r") as file:          # opening the file in read mode
    line = file.readline()                  # reading the contents of the file
    word = line.split(' ')                  # splitting the words of the line

print("The file line is:", line)        # printing the original content
count = 0                               # initializing the counting variable
for i in word:                          # checking the first letter of each word
    if i[0].lower() in ["a", "e", "i", "o", "u"]:       # checking for vowel
        count = count + 1               # increasing counting variable if vowel found

print("The number of words with vowel is:", count)
