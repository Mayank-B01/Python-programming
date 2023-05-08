try:
    num1 = int(input("enter a number"))
    num2 = int(input("enter a num"))
    if num2 == 0:
        raise ZeroDivisionError("You entered zero. Not valid")
    else:
        div = num1/num2
        print(div)
except Exception as e:
    print("Error:", e)
