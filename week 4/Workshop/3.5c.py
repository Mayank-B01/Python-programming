# asking user to input credits
cred = int(input("Enter the college credits earned: "))
# comparing user input and displaying status accordingly
if cred >= 90:
    print("Senior status")
elif cred >= 60:
    print("Junior status")
elif cred >= 30:
    print("Sophomore status")
else:
    print("Freshman status")
