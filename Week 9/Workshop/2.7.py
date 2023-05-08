try:
    lst = ["Mayank", 21, "Oscar", 23, "Hanok"]       # creating list of five elements
    print("The sixth element is", lst[5])                  # printing sixth element
except IndexError:                                         # exception handling for index error
    print("Index is out of range")
    