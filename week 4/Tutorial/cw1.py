#prompting user to input a number
num=float(input("Enter a number"))
#using nested if-esle to check whether number is divisible by 2 and 3

if num%2==0 and num%3==0 :
    print ("The number is divisible by 2 and 3 both")
else:
    print ("The numbr is not divisible by 2 and 3 both")