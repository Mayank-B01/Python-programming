#This program checks whether you can resit for exam

#prompting user to input total working days
w_days=int(input('Enter the number of working days:'))

#prompting user to input absent days
a_days=int(input('Enter the number of absent days'))

#calculating the percentage of class attended
class_per=(a_days/w_days)*100

#displaying absent persentage
print("Absent percentage=",format(class_per,'.2f'))

#checking if the user can resit exam
if class_per <80:
    print ("You cannot resit for the exam")
