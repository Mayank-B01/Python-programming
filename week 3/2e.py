#defining a function to calculate mode, mean and median
def improved_average(n1,n2,n3,n4,n5):
    #importing  library (statistics) function
    import statistics
    #creating a list 
    values=[n1,n2,n3,n4,n5]
    mode_val=statistics.mode(values)
    mean_val=statistics.mean(values)
    median_val=statistics.median(values)
    return mode_val,mean_val,median_val

#asking user to input the five numbers
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
num4=float(input("Enter fourth number:"))
num5=float(input("Enter fifth number:"))

#calling the function
mode_val,mean_val,median_val=improved_average(num1,num2,num3,num4,num5)

#printing the required answers
print("The mode is",mode_val)
print("The mean is",mean_val)
print("The median is",median_val)
