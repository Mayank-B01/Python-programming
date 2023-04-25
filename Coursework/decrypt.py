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


msg = input("Enter message")
shi = int(input("enter shift number"))
print(decrypt(msg.upper(), shi))
