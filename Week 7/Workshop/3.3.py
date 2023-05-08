# defining a function to count letter e
def counting(line):
    counter_num = 0         # initializing counting variable
    for word in line:   # accessing every word
        for letter in word:     # accessing every letter
            if letter.lower() == "e":       # checking letter 'e'
                counter_num = counter_num + 1       # increasing count
            else:
                counter_num = counter_num
    return counter_num


with open("original_text.txt", "r") as file:        # opening the file in read mode
    lines = file.readlines()                        # reading every line of the file


result = counting(lines)                            # calling the function
print("the number of times letter E occured:", result)      # printing the count
          