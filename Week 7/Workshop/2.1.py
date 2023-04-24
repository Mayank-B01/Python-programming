def reduce_spaces(line):
    file = open(line, 'r')
    file_lst = file.read()
    words = file_lst.split("")
    print(words)
    lst = []
    for spc in words:
        lst.append(spc)
        while " " in lst:
            lst.remove(" ")
            print(lst)

    file.close()


print(reduce_spaces(input("Enter the file name")))

