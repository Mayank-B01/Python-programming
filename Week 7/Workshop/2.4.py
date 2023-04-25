f_name = input("Enter file name:")
file = open(f_name, "r")
line = file.read()
file.close()


def count_letters(lines):
    lst=[]
    count = 1
    found = True
    f_line = (lines.lower()).split(" ")
    for letter in f_line:
        for word in letter:
            lst.append(word)
            count = dic[letter]
        else:
            dic[letter] = count

    print(dic)

count_letters(line)