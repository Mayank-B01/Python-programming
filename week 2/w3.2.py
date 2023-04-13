


#Prompting to input weight and height

weight=int(input("Enter the weight in kilograms:"))
height=float(input("Enter height in meter:"))

#converting to floating

weight=float(weight)

#BMI Conversion

BMI=(weight)/(height)**2

#display BMI

print("Weight=",weight)
print("height=",height)
print("The user body mass index is:",BMI)
