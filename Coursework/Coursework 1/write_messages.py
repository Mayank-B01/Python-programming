def write_messages(lst_strings):
    """This function write contents of encrypted / decrypted file from list to a new text file"""
    while True:
        file = input("Output written to:")
        with open(file, "w") as new_file:
            for letter in lst_strings:
                new_file.write(letter)
            print("Message added successfully")
            break
