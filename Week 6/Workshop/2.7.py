# defining a function
def add_daily_temp(dic_1, temp_val, day):
    # checking if the data for that day is present or not
    if day not in dic_1:
        dic_1[day] = temp_val
    return dic_1


# defining an empty dictionary
temp = {}
# asking user if he/she wants to add to the dictionary
choice = ''
# creating a loop for user input in the dictionary
while True:
    # calling function as well as adding key and values to the dictionary
    temp = add_daily_temp(temp, input("Enter the temperature:"), input("Enter the day for the week"))
    choice = input("Do you want to stop?")
    if choice.lower() == "y" or choice.lower() == "yes":
        break
    else:
        continue
print(temp)


