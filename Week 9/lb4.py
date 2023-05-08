try:
    num1 = "a"
    num2 = "b"
    div= num1/num2
    print(div)
except (ValueError, ZeroDivisionError,TypeError) as e:
    print(e)