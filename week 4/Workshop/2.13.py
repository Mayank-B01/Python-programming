# asking user to input height and weight
height = float(input("Enter your height in meter:"))
weight = float(input("Enter your weight in kilograms:"))
# Calculating the BMI of the user
BMI = weight/(height**2)
print("Your BMI is ",format(BMI, '.2f'))
# checking the given condition
if BMI < 18.5:
    print("You are underweight.")
elif (BMI >= 18.5) and BMI < 25:
    print("You have normal weight")
elif 25 <= BMI < 30:
    print("Your are overweight")
else:
    print("You are obese")
