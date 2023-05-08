with open("original_text.txt", 'r') as file1:       # opening original file in read mode
    lines = file1.readlines()                       # reading every line
    with open("new_text.txt", "w") as file2:        # opening new file to write
        for i in range(0, len(lines), 2):           # using loop to select every other line
            file2.write(lines[i])                 # writing original file every other line to new file
