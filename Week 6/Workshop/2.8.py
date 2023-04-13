# creating two dictionaries
dic_1 = {1: 10, 2: 20}
dic_2 = {3: 30, 4: 40}
dic_3 = {5: 50, 6: 60}
# creating a new empty dictionary
new_dic = {}
# using loop to concat the dictionaries
for data in dic_1, dic_2, dic_3:
    new_dic.update(data)
# printing the dictionary
print(new_dic)
