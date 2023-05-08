# importing exists function to check whether the file exits or not
from os.path import exists


def welcome():
    """This functions displays the welcome message to the user"""
    print('''
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher.''')


def enter_shift():
    """This function asks user for the shift number input
       and checks whether the input is valid or not"""
    while True:     # using loop for valid shift input
        shift = int(input("What is the shift number:"))     # asking user to inout shift number
        if 1 < shift < 25:      # for valid condition
            return shift
        else:                   # for invalid condition
            print("Invalid Shift")
            continue


def enter_message():
    """This functions asks the user input for what they want to perform
        encryption/decryption and the number they want to shift by. It also
        checks if the input for mode of encryption is valid or not"""
    while True:     # using loop in case of invalid input
        choice_ed = input('Would you like to encrypt (e) or decrypt (d)').lower()
        if not (choice_ed == 'e' or choice_ed == 'd'):  # checking for valid input
            print('Invalid Mode')
        else:
            if choice_ed == 'e':   # condition for encryption
                text_input = input('What message would you like to encrypt:').upper()
            else:  # condition for decryption
                text_input = input('What message would you like to decrypt:').upper()
            return choice_ed, text_input        # returning conversion mode and message


def encrypt(message, shift):
    """This function encrypts the message by the input shift number and
         returns the encrypted message"""
    e_message = ""
    for char in message:    # traversing the string
        if char.isalpha():
            new_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))  # encrypting the string
            e_message += new_char
        else:           # case for characters other than alphabets
            e_message = e_message + char
    return e_message        # returns encrypted string


# Function to decrypt a cipher text message
def decrypt(message, shift):
    """This function decrypts the message by the shift number input
        by the user and returns the decrypted message"""
    d_message = ""
    for char in message:         # traversing the string
        if char.isalpha():      # checking if the character is alphabet
            new_char = chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))      # decrypting the string
            d_message = d_message + new_char
        else:           # case for characters other than alphabets
            d_message += char
    return d_message         # returns decrypted string


def is_file(file_name):
    """This function checks whether the file exists or not and returns Boolean value"""
    return exists(file_name)


def process_file(file_name, mode, shift_number):
    """This functions encrypts / decrypts the lines in a file and store
       them in a list"""
    with open(file_name, 'r') as file1:     # opening file in read mode
        temp_list = []              # creating empty list
        if mode == 'e':             # for encryption case
            for line in file1:      # traversing the file
                for character in line:      # traversing the string
                    temp_character = encrypt(character.upper(), shift_number)       # encrypting the string by calling the function
                    temp_list.append(temp_character)            # adding to the list
        else:           # for decryption case
            for line in file1:
                for character in line:
                    temp_character = decrypt(character.upper(), shift_number)       # decrypting the string
                    temp_list.append(temp_character)
        return temp_list        # returning the list


def write_messages(all_characters):
    """This function write contents of encrypted / decrypted file from list to a new text file"""
    while True:
        write_file = input('Output written to:')    # taking new file name from the user
        with open(write_file, 'w') as file2:        # opening file in write mode
            for character in all_characters:
                file2.write(character)          # adding list elements to the file
            print('\nFile saved successfully')
            break


def message_or_file():
    """This function determine whether the program will cipher a message in console or file"""
    while True:
        choice_ed = input('Would you like to encrypt (e) or decrypt (d):').lower()      # asking choice for what typ of conversion
        if choice_ed != 'e' or choice_ed != 'd':      # Invalid input case
            print('Invalid Mode')
            continue
        else:               # valid input case
            while True:
                choice_type = input('Would you like enter in console (c) or file (f):').lower()     # asking whether converting message or file
                if choice_type != 'c' or choice_type != 'f':  # case for invalid input
                    print('Invalid Mode')
                    continue
                else:       # valid input case
                    if choice_type == 'c' and choice_ed == 'e':         # case for console and encryption
                        text_input = input('What message would you like to encrypt:').upper()   # asking and changing text to upper case
                        file_name = None                # setting file case to None
                    elif choice_type == 'c' and choice_ed == 'd':
                        text_input = input('What message would you like to encrypt:').upper()
                        file_name = None             # setting file case to None
                    else:   # case for file
                        file_name = input('What message would you like to decrypt:').upper()
                        text_input = None
                return choice_ed, text_input, file_name


def want_to_continue():
    """This function allows user to use the program as much as they want"""
    while True:
        try:
            # prompt user to input if they want to continue
            repeat = input("Do you want to continue (y)es or (n)o:")    # asking user choice
            if not (repeat == 'y' or repeat == 'n'):
                raise Exception     # raising exception if it is invalid input
            elif repeat == "y":
                return True     # returning condition to run the program again
            elif repeat == "n":
                return False  # returning the condition to stop the program
        except Exception:  # displaying statement if invalid input is entered
            print("Invalid input!")


def main():
    welcome()  # call welcome function
    still_continue = True
    run_file = False
    while still_continue:
        if run_file:
            choice, message, file1 = message_or_file()  # call message_or_file function
        else:
            choice, message = enter_message()  # call enter message function
            file1 = None
        shift_number = enter_shift()  # call enter_shift function
        if file1 is None:
            if choice == 'e':
                print(encrypt(message, shift_number))
            else:
                print(decrypt(message, shift_number))
        else:
            while not is_file(file1):
                print('File not found{Fore')
                file1 = input('What is the name of the file:').upper()
            # call process_file function
            changed_text_list = process_file(file1, choice, shift_number)
            write_messages(changed_text_list)
        if still_continue:
            run_file = True
            still_continue = want_to_continue()  # call want_to_continue function
            continue
    print('Thank you for using my program')


main()  # call main function
