try:
    amount = int(input("Enter the amount:"))
    if amount < 10000:
        raise ValueError("Your amount is less than 10000")
    else:
        print("The amount is:", amount)
except ValueError as e:
    print(e)
    