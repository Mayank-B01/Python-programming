#defining a function
def hello_world(name):
     """This function prints a message of 'Hello World' with name"""
     print ("Hello World,my name is",name,".")

#asking user to input name

name=input("Please enter your name:")

#printing docstring
print(hello_world.__doc__)

#calling function

hello_world(name)
