with open("file.txt", "r") as file:  # opening the file
    line1 = file.readline()         # reading the first line
    line2 = file.readline()         # reading the second line
print("line1 =", line1, "line2 =", line2)


# defining a function to arrange the characters
def interleave_chars(lin1, lin2):
    lst1 = []       # creating an empty list
    lst2 = []       # creating another empty list
    for i in lin1.strip("\n"):  # creating a loop to make list of first line
        lst1.append(i)          # adding characters of line1 to the list
    lst1.append('')
    lst1.append('')
    for j in lin2.strip("\n"):  # loop for list of characters of second line
        lst2.append(j)          # adding character of second line to the second list
    for k in range(0, len(lst2)):    # loop for joining the characters
        result = lst1[k] + lst2[k]  # joining single element of each list
        print(result, end='')       # printing the single string


# calling the function
interleave_chars(line1, line2)
