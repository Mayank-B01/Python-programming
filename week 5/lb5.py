while True:
    name=input("Enter your name")
    age=int(input("Enter your age"))
    quali=input("Enter your qualification")
    contact=int(input("Enter you contact number"))
    address=input("Enter your address")
    email=input("Enter email address")
    salary_exp = int(input("Enter your salary expectaton"))
    exp=int(input("Enter experience"))
    if salary_exp > 20000:
        print("your enquiry recorded,your exp must be at least 2 years")
        if exp > 2:
            print("you are short listed")
    elif salary_exp < 20000 and exp < 2:
        print("your enquiry recorded.we will notify")
    else:
        print("your choice is recorded")

    add=input("Do you want to add more?")
    if add.lower() == "y":
        continue
    else:
        print("all data are entered")
        break