file_name = input("Enter file name:")
with open(file_name,"r") as file:
    print(file.read())
f_ile = open(file_name,"r")
print(f_ile.read())
f_ile.close()