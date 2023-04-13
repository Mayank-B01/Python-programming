def reduce_spaces(line):
    file = open(line, 'r')
    file_lst = file.readline()
    for letter in file_lst:
        if letter ==" ":
            letter.replace(" ", "")
    return file_lst
    file.close()


print(reduce_spaces(input("Enter the file name")))

