units = int(input("Enter a number"))
if units <= 100:
    print("No charge")
elif 100 < units <= 200:
    n_unit = units - 100
    cost = n_unit * 5
    print("Your cost is Rs.", cost)
else:
    cost = 100 * 5
    a_unit = units - 200
    a_cost = a_unit * 10
    t_bill = cost + a_cost
    print("your bill is Rs.", t_bill)
