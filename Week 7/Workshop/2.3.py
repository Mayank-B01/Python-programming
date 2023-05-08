# defining a function
def check_quotes(lines):
    single_quote = 0
    double_quote = 0
    for label in lines:
        if label == "'":
            single_quote = single_quote + 1
        elif label == '"':
            double_quote = double_quote + 1
        else:
            single_quote = single_quote
            double_quote = double_quote
    if single_quote > 1 or double_quote > 1:    # condition for checking only one quote mark
        if single_quote % 2 == 0 and double_quote == 0:
            print(True)
        else:
            print(False)
    else:
        print(True)


file_name = input("Enter file name:")       # asking user to input file name
file = open(file_name, "r")     # opening the file
line = file.read()      # reading the file
file.close()            # closing the file
check_quotes(line)
