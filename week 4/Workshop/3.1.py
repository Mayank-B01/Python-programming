# defining a function to return product
def mult(x, y):
    # using if else statement to check condition
    if x > 0 and y > 0:
        prod = x * y
        return prod
    else:
        prod = 0
        return prod


# asking user to input numbers
num1 = int(input('Enter first number:'))
num2 = int(input('Enter the second number:'))
# calling the function
product = mult(num1, num2)
# printing the result
if product == 0:
    print("You entered negative number. So the product is", product)
else:
    print("The product of the two numbers is", product)
