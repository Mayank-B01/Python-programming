from os.path import exists


def continue_again():
    while True:
        try:
            chance = input("Would you like to encrypt or decrypt another message? (y/n):")
            if chance == 'y':
                return True
            elif chance == 'n':
                return False
            else:
                raise Exception
        except Exception:
            print("Invalid input!")


# defining a function to display welcome message
def welcome():
    """This functions displays the welcome message to the user"""
    print('''
    Welcome to the Caesar Cipher
    This program encrypts and decrypts text with Caesar Cipher''')


# defining a function to check the validity of shift number
def shift_val():
    """This function asks user for the shift number input
    and checks whether the input is valid or not"""
    while True:
        shift = int(input("What is the shift number:"))
        if 1 < shift < 25:
            return shift
        else:
            print("Invalid Shift")
            continue


# defining a function for user input
def enter_message():
    """This functions asks the user input for what they want to perform
    encryption/decryption and the number they want to shift by. It also
    checks if the input for mode of encryption is valid or not"""
    while True:
        # asking user input for encrypt or decrypt
        choice = input(" Would you like to encrypt(e) or decrypt(d):")
        if choice.lower() == "e":
            # asking user to input the message
            message = input("What message would you like to encrypt:")
            return message.upper(), choice
        elif choice.lower() == "d":
            message = input("What message would you like to decrypt:")
            return message.upper(), choice
        else:
            print("Invalid Mode")
            continue


# defining encrypt function
def encrypt(message, shift):
    """This function encrypts the message by the input shift number and
     returns the encrypted message"""
    new_word = ''
    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(letter)
            new_num = num + shift
            new_word = new_word + chr(new_num)
        else:
            new_word = new_word + letter
    return new_word


def decrypt(message, shift):
    """This function decrypts the message by the shift number input
    by the user and returns the decrypted message"""
    new_message = ''
    for word in message:
        if word in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(word)
            new_num = num - shift
            new_message = new_message + chr(new_num)
        else:
            new_message = new_message + word
    return new_message


def process_file(f_name, s_mode):
    """This functions encrypts / decrypts the lines in a file and store
    them in a list"""
    lst = []
    with open(f_name, "r") as file:
        shift = shift_val()
        if s_mode == "e":
            for line in file:
                for word in line:
                    message = encrypt(word.upper(), shift)
                    lst.append(message)
        else:
            for line in file:
                for word in line:
                    message = decrypt(word.upper(), shift)
                    lst.append(message)
    return lst


def is_file(file_name):
    """This functions checks whether the file exists or not and returns Boolean value"""
    return exists(file_name)


def write_messages(lst_strings):
    """This function write contents of encrypted / decrypted file from list to a new text file"""
    while True:
        file = input("Output written to:")
        with open(file, "w") as new_file:
            for letter in lst_strings:
                new_file.write(letter)
            print("Message added successfully")
            break


def message_or_file():
    while True:
        choice = input("Would you like to encrypt(e) of decrypt(d)?:")
        if choice != "e" or choice != "d":
            print("Invalid mode")
            continue
        else:
            while True:
                choice_mode = input("Would you like to read from a file(f) or the console(c)?:")
                if choice_mode != "c" and choice != "f":
                    print("Invalid Mode")
                    continue
                else:
                    if choice_mode == "c" and choice == "e":
                        text = input("What message would you like to encrypt:")
                        file = None
                    elif choice_mode == "c" and choice == "d":
                        text = input("What message would you like to decrypt:")
                        file = None
                    else:
                        text = None
                        file = input("Enter a file name:")
                return choice, text, file


def main():
    welcome()
    run_again = True
    file_run = False
    while True:
        if file_run:
            choice, message, file = message_or_file()
        else:
            message, choice = enter_message()
            file = None
        shift = shift_val()
        if file is None:
            if choice == "e":
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))
        else:
            while not is_file(file):
                print("File not found")
                file = input("Enter file name:")
            file_change = process_file(file, choice)
            write_messages(file_change)
        if run_again:
            file_run = True
            run_again = continue_again()
            continue
    print("Thank You for using Caesar Cipher. Goodbye!! ")


main()
