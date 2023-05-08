try:
    num1 = int(input("Enter any number:"))      # asking user input
    num2 = int(input("Enter any number:"))
    add = num1 + num2                           # performing sum
except Exception as e:                          # exception handling
    print("Error:", e)
else:                                           # case for no exception
    print("The sum is", add)
