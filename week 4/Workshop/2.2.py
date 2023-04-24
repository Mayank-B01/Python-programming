# This program calculates the grade according to input percentage
# asking user to input percentage
percent = float(input("Enter your percentage:"))
# displaying grade by checking percentage
if percent > 90:
    print("Your grade is A")
elif 80 < percent <= 90:
    print("Your grade is B")
elif 60 <= percent <= 80:
    print("Your grade is C")
else:
    print("Your grade is D")
