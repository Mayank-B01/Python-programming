def read_file(filename):
    with open(filename,'r') as file:
        data = file.read()
    return data
def write_file(filename,data):
    with open(filename,'w') as file:
        file.write(data)

filename='Hello.txt'
file_data = read_file(filename)
print(file_data)
new_data = "This is some new text."
write_file(filename,new_data)
print(write_file.read())
