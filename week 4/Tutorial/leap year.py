#This program check whether a year is a leap year or not

#prompting user to input year

year=int(input("Enter the year:"))

#using if-else statement

if year % 4 ==0 :
    print ("It is a leap year")
else:
    print("It is not a leap year")