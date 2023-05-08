file = input("Enter file name:")        # asking user for a file name
with open(file, "r") as files:          # opening the file in read mode
    line = files.read()                 # reading the contents of the file
    for month in line.split():          # separating each line of the file using split function
        print(month[0:3])               # printing the first three letter of each line



