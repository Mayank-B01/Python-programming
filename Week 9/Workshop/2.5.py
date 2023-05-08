try:
    lst = []
    while True:
        num = int(input("Enter a number"))      # asking user input
        lst.append(num)                         # making a list of user input
        choice = input("Press y or yes to continue or any keys to quit:")
        if choice.lower() == "y" or choice.lower() == "yes":  # condition for adding more user input
            continue
        else:
            break
    print(lst)
    add = 0                             # initializing variable to store sum
    for j in range(len(lst)):           # using loop to add list elements
        add = add + lst[j]              # sum of list elements
    print(add)                          # printing sum
except Exception as e:                  # exception handling
    print("Error:", e)
