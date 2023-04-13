# prompting the user to enter integers and store them in a list
num1 = int(input("Enter first integer:"))
num2 = int(input("Enter second inter"))
num3 = int(input("Enter third number"))
num_lst = [num1, num2, num3]
print("Before edit list=", num_lst)
for i in range(len(num_lst)):
    if num_lst[i] > 100:
        (num_lst[i]) = 'over'
print("After edit=", num_lst)
