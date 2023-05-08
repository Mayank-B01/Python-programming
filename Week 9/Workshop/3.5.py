def number(num):
    try:
        if not num:
            raise ValueError("The list is empty")
        large = num[0]
        for i in num:
            if i > large:
                large = i
        return large
    except Exception as e:
        print(e)


lst = [5, 6, 8]
largest = number(lst)
print("The largest number in the list is", largest)
