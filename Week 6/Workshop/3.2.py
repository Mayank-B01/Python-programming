# creating two integer list
lst_1 = {5, 4, 2, 8}
lst_2 = {1, 2, 4, 5}
# finding the common elements
new_lst = set(lst_1).intersection(lst_2)
print("First list:", lst_1)
print("Second list:", lst_2)
print("List with common integers:", new_lst)
