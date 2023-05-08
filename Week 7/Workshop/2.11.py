ss_num = input("Enter the social security number")     # asking user for social security number
for i in ss_num:                    # using loop to access every character
    result = i.isdigit()            # checking if the character is digit
    if not result:
        status = True               # status if non-digit character found
        break
    else:
        status = False
        continue
if status:                          # checking status and printing relevant message
    print("The security number contains non-digits")
else:
    print("The security number does not contain non-digits")
