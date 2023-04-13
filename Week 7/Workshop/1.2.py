# openinfg a file to write
output_file = open("datafile2.txt", 'w')
output_file.write("This is a new file")
output_file.close()
# opening the file to read the text file contents
file = open("datafile2.txt", 'r')
print(file.readline())
file.close()
