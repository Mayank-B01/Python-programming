# defining a function to return top three items using built-in function
def top_item(item_dic):
    item_dic = sorted(item_dic.items(), key=lambda item: item[1])
    print(item_dic[2:5])


# creating a dictionary
item_lst = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
# calling the function
top_item(item_lst)


