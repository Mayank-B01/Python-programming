try:
    numerator = int(input("Enter a number"))
    denominator = int(input("Enter a number"))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0")
except ValueError:
    print("Error: Invalid integers")
except Exception as e:
    print(e)



