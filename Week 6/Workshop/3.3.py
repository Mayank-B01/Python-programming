# creating a dictionary
dic_1 = {"Mayank": 20, "Oscar": 23, "Ishwor": 17, "Sumit": 17}
# creating an empty dictionary to store people over 18
new_dict = {}
# checking people over 18
for name, age in dic_1.items():
    if age >= 18:
        new_dict[name] = age

print(new_dict)