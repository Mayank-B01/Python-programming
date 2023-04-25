def reduce_spaces(line):
    words = line.split()
    lst = []
    for spc in words:
        lst.append(spc)
    while " " in lst:
        lst.remove(" ")
    string = ""
    for j in lst:
        string = string + j
    print(string)


file_name = input("Enter file name:")
file = open(file_name, 'r')
file_lst = file.read()
print(reduce_spaces(file_lst))

