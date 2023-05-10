try:
    file_name = input("Enter file name:")       # asking user to input file name
    with open(file_name, "r") as file:          # opening the file in read mode
        line = file.read()                      # reading the contents of the file
        print(line)
except IOError:                                 # exception handling if the file does not exist
    print("The file does not exists.")
