# defining a function to check key and value
def check_list(lst, key_chk, value_chk):
    found = False
    for keys in lst:
        for key, val in keys.items():
            if key_chk.lower() == key.lower() and value_chk.lower() == val.lower():
                found = True
                print("Key:", key_chk, "and Value:", value_chk, "exists")
                break
    if not found:
        print("Key:", key_chk, "and Value:", value_chk, "does not exists")


# creating list with each element a dictionary
student = [{"student id": 1, "name": "Jean Castro", "class": "V"},
           {"student id": 2, "name": "Lula Powell", "class": "V"},
           {"student id": 3, "name": "Brian Howell", "class": "VI"},
           {"student id": 4, "name": "lynne Foster", "class": "VI"},
           {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# asking input for key and value
key_val = input("Enter the key:")
val_input = input("Enter the value:")
# calling the function
check_list(student, key_val, val_input)
