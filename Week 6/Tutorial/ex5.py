def add_book(b_name):
    lib.append(b_name)
    print(b_name,"has been added")
def remove_book(b_name):
    lib.remove(b_name)
    print(b_name, "has been removed")
def search_book(b_name):
    foundBook = False
    for book in lib:
        if book == b_name:
            foundBook = True
    if foundBook == True:
        print(b_name, "found")
    else:
        print(b_name, "did not found.")
def all_book():
    print(lib)
lib = [1,2,3]
again = True
while again:
    choice=input("Enter your choice:")
    if choice == "1":
        b_name=input("Enter the book name")
        add_book(b_name)
    elif choice == '2':
        b_name = input("Enter the book name")
        remove_book(b_name)
    elif choice == '3':
        b_name = input("Enter the book name")
        search_book(b_name)
    elif choice == '4':
        all_book()
    else:
        again = False
        print("You have exit the library")