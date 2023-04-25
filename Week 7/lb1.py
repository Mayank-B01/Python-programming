f_name = input("enter file name:")
file_n = open(f_name,"r")
print(file_n.read())
file_n.close()