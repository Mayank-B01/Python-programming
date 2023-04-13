#defining a function

def types(num):
    '''This function prints float and integer value of a number'''
    print("The float value is",float(num))
    
    print("The integer value is",int(num))
    
#Calling the function
print(types.__doc__)
types(input("Enter a number:"))
