try:
    city = input("Enter any city:")     # prompting user to input a city name
    # checking the user input in a list
    if city.lower() not in ['kathmandu', 'ktm', 'pokhara', 'pkh', 'nepalgunj', 'npj', 'birgunj', 'brj']:
        raise ValueError    # raising error if the input is invalid
    else:
        if city.lower() == "kathmandu " or city.lower() == 'ktm':  # comparing user input with list elements
            print("Pashupatinath temple")
        elif city.lower() == "pokhara" or city.lower() == "pkh":
            print("Fewa Lake")
        elif city.lower() == "nepalgunj" or city.lower() == "npj":
            print("Bageshwori Temple")
        else:
            print("Birgunj Ghanta Ghar")
except ValueError:
    print("Please enter valid city")
