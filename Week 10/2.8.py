def unique_list(lst):       # defining a function
    for i in range(len(lst)):       # running a loop for the number of elements
        lst = lst[1:]               # making another list except the first element
        if i in lst:                # checking for the repetition of the element
            return True
    return False


list1 = [1, 2, 2, 5]            # making a list of numbers
print(unique_list(list1))       # calling the function
