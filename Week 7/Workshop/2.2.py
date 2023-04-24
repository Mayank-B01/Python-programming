def extract_temp(letter):
    value = letter.split()
    for val in value:
        if val.isdigit():
            print("The number found is:", val)


sent = input("Enter file name")
lin = open(sent, "r")
line = lin.read()
extract_temp(line)
