# defining a function
def get_weekend_average_teap(temps):
    add = 0
    for temp in temps.values():
        add = add + temp
    avg = format(add / len(temps), '.2f')
    return avg


temp_val = {"Sunday": 21, "Monday": 22, "Tuesday": 25, "Wednesday": 23,
            "Thursday": 20, "Friday": 22, "Saturday": 28}
# printing the average temperature
print("The avaerage weekend temperature is", get_weekend_average_teap(temp_val))
