err_mesg = input("Enter the error message:")        # asking user for error message input
new_msg = err_mesg.strip("*")               # removing '*' from message
final_msg = new_msg.replace(" ", "")        # removing blank space
print(final_msg)                            # printing final result
