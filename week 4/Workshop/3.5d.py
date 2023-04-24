# asking user t input a number
number = int(input("Enter a number: "))
# checking the given conditions using if statements
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Number neither divisible by 3 or 5")
