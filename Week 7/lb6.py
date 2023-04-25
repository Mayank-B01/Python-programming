
while True:
    # Get user input for form data
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    inquiry = input("Enter your inquiry: ")

    # Create a dictionary to store form data
    form_data = {
        "Name": name,
        "Email": email,
        "Inquiry": inquiry
    }

    # Open the file in write mode and write form data to the file
    with open("form_data.txt", "a") as file:
        for field, value in form_data.items():
            file.write(f"{field}: {value}\n")
    # asking user if they want to input more data
    choice = input("Do you want to continue?")
    if choice.lower() == 'y':
        continue
    else:
        break

with open("form_data.txt", "r") as file:
    print(file.read())
