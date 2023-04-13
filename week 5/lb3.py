condition=True
pos_num=0
while True:
    num=int(input("Enter any number:"))
    if num > 0:
        pos_num= pos_num+ num
        print("you entered positive number")
    elif num<0:
        print("you enteres negative number")
    else:
        print("you entered zero")
    choice= input("Press q to quit or any other ke to continue")
    if choice.lower()=='q':
        break
    else:
        continue

print("the sum is:",pos_num)

