#defining a function

def squared(number):
    '''This function returns the squared value of a number'''
    square=number**2
    return square

#printing docstring
print(squared.__doc__)

#Asking user input and calling function
print( "The squared of the number is",squared(int(input("Enter a number:"))))

