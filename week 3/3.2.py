#defining addition function
def add(num1,num2):
    '''This function adds the two number'''
    sum=num1+num2
    print("The sum is",sum)
#defining subtraction function
def sub(num1,num2):
    '''This function calcualtes the difference of two numbers'''
    dif=num1-num2
    print("The difference is",dif)
#defining multiplication
def mul(num1,num2):
    '''This function finds the product of two numbers'''
    product=num1*num2
    print("The product is",product)
#definig division
def div(num1,num2):
    '''This function calculates the division of two number'''
    division=format(num1/num2,".2f")
    print("The division is",division)
#defining modulus
def mod(num1,num2):
    '''This function finds the modulus of two number'''
    modulus=num1%num2
    print("The modulus is",modulus)
#defining exponentiation
def exp(num1,num2):
    '''This function calculates the exponentiation of num1 to num2'''
    expo=num1**num2
    print("The exponentiation is",expo)
#Displaying welcome message
print ("Hello! Welcome to Calculator")
#user input num1 and num2
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
#calling the function
help(add)
add(num1,num2);print("\n")
help(sub)
sub(num1,num2);print("\n")
help (mul)
mul(num1,num2);print("\n")
help(div)
div(num1,num2);print("\n");help(mod)
mod(num1,num2);print("\n");help (exp)
exp(num1,num2)
          
