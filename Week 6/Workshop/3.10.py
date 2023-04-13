# defining a function to remove common elements
def remove_lst(ls1, ls2):
    empty_lst = []
    for val in ls1:
        if not val in ls2:
            empty_lst.append(val)
    return empty_lst


# creating two list with some same elements
lst1 = ["red", "orange", "green", "blue", "white"]
lst2 = ["black", "yellow", "green", "blue"]
# printing the new list
print("Color1-Color2", remove_lst(lst1, lst2))
print("Color2-Colo1", remove_lst(lst2, lst1))
