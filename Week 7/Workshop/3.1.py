# asking user to input file name
f_name = input("Enter file name:")
# opening the file in read mode
with open(f_name,"r") as file:
    line = file.readlines()     # reading every line in the file and storing as list
    no_of_lines = len(line)     # counting the number of lines by counting the length of list
print("The number of lines:", no_of_lines)
