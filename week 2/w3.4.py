#prompting user to input radius

radius=int(input("Enter the radius:"))

#Calculating total surface area of hemisphere

S_area=3*(22/7)*radius**2

#converting the area to 2 significant digits after decimal
S_area="{:.2f}".format(S_area)

#printing the are

print("The total surface area of hemisphere with radius",radius,"is", S_area)
