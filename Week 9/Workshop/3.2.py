try:
    num = int(input("Enter the numerator:"))
    den = int(input("Enter the denominator:"))
    div = num / den
    print(div)
except ValueError:
    print("Entered value is wrong.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except Exception as e:
    print("Error", e)
