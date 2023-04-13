# defining a function to sort the authors
def sorting(book_lst):
    for i in range(len(book_lst)):
        for j in range(i+1, len(book_lst)):
            if book_lst[j][1] < book_lst[i][1]:
                book_lst[i], book_lst[j] = book_lst[j], book_lst[i]
    return book_lst


# creating a book tuple
book = [("The Harry Potter", "J.K. Rowling"), ("Two States", "Chetan Bhagat"),
        ("The Chronicles of Narnia", "C.S Lewis")]
# calling the function
print(sorting(book))