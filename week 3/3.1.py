#defining a function

def num_div():
    '''This function divides the first number by secon number'''
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    div=format(num1/num2,".2f")
    print("The division of first number by second number is",div)

#printing the docstring
print(num_div.__doc__)

#calling the function
num_div()

