# defining a function to count each character
def count_letters(lines):
    lst = {}        # creating a dictionary to count and store each character uniquely
    for letter in lines:    # checking each character
        if letter.isalpha():    # checking if the character is alphabet or not
            letter = letter.lower() # converting every character to lower case to count same alphabets
            if letter not in lst:       # condition for finding alphabet for first time
                lst[letter] = 1
            else:                       # condition for finding same alphabet again
                lst[letter] = lst[letter] + 1
    return list(lst.items())            # returning the dictionary in the form of list


f_name = input("Enter file name:")      # asking user input for file name
file = open(f_name, "r")            # opening the file in read mode
line = file.read()
file.close()
result = count_letters(line)        # calling the function
print(result)                       # printing the list

