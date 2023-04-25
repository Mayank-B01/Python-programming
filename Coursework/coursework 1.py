from os.path import exists


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
        if choice.lower() == "e" or choice.lower() == "d":
            # asking user to input the message
            message = input("Enter the message")
            shift = shift_val()
            return message.upper(), shift
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


def is_file(file_name):
    """This functions checks whether the file exists or not and returns Boolean value"""
    return exists(file_name)
