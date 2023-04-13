def write_file(filename,text):
    with open(filename,'w') as f:
        f.write(text)

        
filename=input("Enter file name with extnsion:")
text = input("Enter the text to be entered in the file:")

write_file(filename,text)
