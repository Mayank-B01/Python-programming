file_name = input("Enter file name:")       # asking user to input file name
file = open(file_name, "r")     # opening the file
line = file.read()      # reading the file
file.close()            # closing the file


# defining a function
def check_quotes(lines):
    quote = "Today's high temperature will be 75 degrees"
    line1 = quote.split()
    lst1 = []
    for letter in line1:
        lst1.append(letter)
    lst2 = []
    line2 = line.split()
    for label in line2:
        lst2.append(label)

    set1 = set(lst1)
    set2 = set(lst2)
    common = set1.issubset(set2)
    return common


print(line,"=", check_quotes(line))
