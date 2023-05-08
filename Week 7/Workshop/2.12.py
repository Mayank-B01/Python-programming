email_addr = input("Enter your email address:")     # asking user for email address
if '@' in email_addr:           # checking if @ is present
    print("@ was found in", email_addr.index("@"), "index")     # printing index number if found
else:
    print("@ was not found")            # printing not found message
    