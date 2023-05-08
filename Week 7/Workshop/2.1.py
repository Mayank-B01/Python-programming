# defining a function to remove blank spaces
def reduce_spaces(line):
    words = line.split(" ")     # using split function to remove spaces
    print(words)                # displaying the words in the file in list
    string = ""
    for j in words:     # using loop to join the words in the list
        string = string + j     # joining the words after removing spaces
    print(string)               # displaying the lines after removing spaces


file_name = input("Enter file name:")       # asking user for file name
file = open(file_name, 'r')     # opening the file
file_lst = file.read()      # reading the file
print(reduce_spaces(file_lst))      # calling the function with file lines as argument
