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

shi = int(input("enter shift number"))
msg = input("Enter the message")
print(encrypt(msg.upper(), shi))

