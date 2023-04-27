def message_or_file():
    while True:
        choice = input("Would you like to encrypt(e) of decrypt(d)?:")
        if choice != "e" or choice != "d":
            print("Invalid mode")
            continue
        else:
            while True:
                choice_mode = input("Would you like to read from a file(f) or the console(c)?:")
                if choice_mode != "c" and choice != "e":
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
                return choice, text.upper(), file

