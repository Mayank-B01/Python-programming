#defining a function to change integer to string

def int_to_string(num):
    '''This function converts integer data to string data'''
    num=str(num)
    return num

#printing the docstring
print(int_to_string.__doc__)

#assigning an integer number
num=int(input("Enter an integer number:"))

#checking data type
print(type(num))

#calling the function
print(int_to_string(num))

#assigning variable to check changed data type
n_str=int_to_string (num)
print (type(n_str))

