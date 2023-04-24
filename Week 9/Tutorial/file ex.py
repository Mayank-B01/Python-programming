try:
    with open("example.txt", "w") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("File access denied")
except Exception as e:
    print(f"An error occurred:{e}")
