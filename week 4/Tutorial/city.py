# asking user to input city
city = input("Enter the city:")

#using nested if to print monuments
if city == "kathmandu" or city=='ktm' or city=='k':
    print('Pashupatinath Temple')
else:
    if city=='pokhara' or city=='pkh' or city=='p':
        print ('Fewa Lake')
    else:
        if city=='neaplgunj' or city=='npj' or city=='n':
            print('Bageshwori Temple')
        else:
            if city=='birjumg' or city == 'brj' or city == 'b':
                print ("Birgunj Ghanta ghar")
            else:
                print ('none')
