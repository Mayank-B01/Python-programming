# this program prints the fibonacci series for the number of inputs the user enters
# asking user to input the number of terms needed
num = int(input("Enter the number of terms needed: "))
# initializing variables to display the fibonacci series
n1 = 1
n2 = 1
val = 0
# creating a loop to display fibonacci series
for i in range(num):
    print(n2)
    val = n1
    n1 = n1 + n2
    n2 = val

