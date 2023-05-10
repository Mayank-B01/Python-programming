try:
    num = int(input("Enter a number"))      # asking the user to input a number
except Exception as e:      # handling the exception
    print("Error", e)
