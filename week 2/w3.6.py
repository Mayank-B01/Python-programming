#prompt the user to assign the grades for three exam

grade1=int(input("Enter the first grade of the student:"))
grade2=int(input("Enter the second grade of the student:"))
grade3=int(input("Enter the third grade of the student:"))

#calculating and print the average grade

avg_grade=(grade1+grade2+grade3)/3
print("The average grade of the student is:",avg_grade)
