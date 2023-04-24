temperature = float(input("Enter the temperature:"))
humidity = float(input("Enter the humidity:"))
if temperature >= 85 and humidity > 60:
    print("Muggy day today")
elif temperature >= 85:
    print("Warm, but not muggy today")
elif temperature >= 65:
    print("pleasant today")
elif temperature <= 45:
    print("cold today")
else:
    print("Cool today")