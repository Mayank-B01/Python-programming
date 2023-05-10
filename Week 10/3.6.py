import csv      # importing the csv module
path = "student.csv"    # assigning the file name to a variable
with open(path, 'r') as file:       # opening the file in read mode
    lines = csv.reader(file)       # reading the csv file
    stud = list(lines)[1:]      # storing the contents of line as a list except the first element
    for students in stud:   # accessing the data in the list
        # using format function for storing the calculation
        avg = format((int(students[1]) + int(students[2]) + int(students[3])) / 3, '.2f')
        print(students[0], avg)
