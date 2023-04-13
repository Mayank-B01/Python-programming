num=int(input("enter a num"))
while True:
    if num < 0:
        print("Enter again")
        num=int(input("enter num"))
    else:
        for i in range(1,11):
            print(num,'*', i, '=', num*i)
        break
