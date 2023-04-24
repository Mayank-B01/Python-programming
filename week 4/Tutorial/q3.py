# This program display grade according to the percentge

# prompting user to input percentage
percent = float(input("Enter your percentage:"))

# using if=elif statement to display grade

if percent >= 70:
    print("Grade A")
elif percent >= 60:
    print("Grade B")
elif percent >= 50:
    print("Grade c")
else:
    print("fail")
