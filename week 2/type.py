#aking user to imput two numbers

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

#addition
print("Sum:",num1+num2)

#subtraction
print("Subtraction:",num1-num2)

#multiplication
print ("Multiplication:",num1*num2)

#division
print("Division:",num1/num2)

#Enter weight and height

Weight=input("enter the weight in pounds:")
Height=input("enter the height in inches:")

#converting to floating

weight=float(Weight)
height=float(Height)

#BMI Conversion

BMI=(weight *703)/(height)**2

#display BMI

print("The user body mass index is:",BMI)

