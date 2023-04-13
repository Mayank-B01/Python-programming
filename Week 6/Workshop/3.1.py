# creating a string list
str_lst = ["Ishwor", "Mayank", "Sumit", "Oscar"]


# defining a function to create a new list with only letter a string
def string_a(string_lst):
    new_lst = []
    for val in string_lst:
        for letter in val.lower():
            if letter == "a":
                new_lst.append(val)
                break
    return new_lst


print(string_a(str_lst))
