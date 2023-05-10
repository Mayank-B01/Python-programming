def unit_sold(product):     # defining a function to calculate total units sold
    total = 0               # initializing total value
    for items in product:      # accessing every value of dictionary
        unit = int(items["UnitSold"])       # accessing items of dictionary
        total = total + unit            # calculating the total units sold
    return total


def revenue(product):       # defining a function to calculate total revenue
    total_revenue = 0
    for item in product:    # accessing the items of the dictionary
        pro_revenue = int(item['UnitSold']) * int(item['UnitPrice'])  # accessing the items of each element
        total_revenue = total_revenue + pro_revenue     # calculating total revenue
    return total_revenue


with open("sales.txt", "r") as file:       # opening file in read mode
    product = file.readlines()      # reading the contents of the file

product_dic = []        # creating an empty list
for index, products in enumerate(product):  # creating a loop to create a dictionary
    temp_dic = {}       # initializing a dictionary
    if index == 0:
        keys = products.split(',')
    else:
        values = products.split(',')
        temp_dic[keys[0]] = values[0]
        temp_dic[keys[1]] = values[1]
        temp_dic[keys[2]] = values[2]
        temp_dic[keys[3]] = values[3]
        temp_dic[keys[4].strip()] = values[4]
        product_dic.append(temp_dic)

print("Total revenue:", revenue(product_dic))
print("Total units sold:", unit_sold(product_dic))
