# using try-except statement for any error handling
try:
    # asking user for file name
    file_name = input("Enter the file name:")
    # opening the file in read mode
    with open(file_name, "r") as file:
        line = file.read()
        print(line)
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("The file can not be accessed")
except Exception as e:
    print("Error:", e)
