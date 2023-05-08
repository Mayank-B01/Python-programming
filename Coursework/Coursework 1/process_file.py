def decrypt(message, shift):
    new_message = ''
    for word in message:
        if word in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(word)
            new_num = num - shift
            new_message = new_message + chr(new_num)
        else:
            new_message = new_message + word
    return new_message


def encrypt(message, shift):
    new_word = ''
    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(letter)
            new_num = num + shift
            new_word = new_word + chr(new_num)
        else:
            new_word = new_word + letter
    return new_word


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


def process_file(f_name, s_mode):
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


file_name = input("Enter file name")
mode = input("Enter the mode")
print(process_file(file_name, mode))
