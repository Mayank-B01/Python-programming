date = input("Enter the date in mm/dd/yyyy format:")    # asking user for date
new_date = date.replace('/','-')                        # replacing the '/' with '-'
print("The formatted date is", new_date)                # printing the formatted date
