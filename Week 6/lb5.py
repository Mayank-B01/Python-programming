dic_1 = {'new york': 'city', 'nepal': 'country', 'kathmandu': 'city', ' New delhi': 'city'}
count1 = 0
count2 = 0
dic_2 ={}
for key in dic_1.values():
    if key == 'city':
        count1 = count1 + 1
        key1 = key
    else:
        count2 = count2 +1
        key2 = key
dic_2[key1] = count1
dic_2[key2] = count2
print(dic_2)
