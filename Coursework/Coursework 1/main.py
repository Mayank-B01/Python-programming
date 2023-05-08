def main():
    welcome()
    file_run = False
    while True:
        if file_run:
            choice, message, file = message_or_file()
        else:
            message, choice = enter_message()
            file = None
        if file is None:
            if choice == "e":
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))
        else:
            while not is_file(file):
                print("File not found")
                file = input("Enter file name:")
            file_change = process_file(file, mode)
            write_messages(file_change)
        Process_again = input("Would you like to encrypt or decrypt another message?"):
        if Process_again.lower() == "y" or Process_again.lower() == "yes":
            continue
        else:
            break
    print("Thank You for using Caesar Cipher. Goodbye!! ")