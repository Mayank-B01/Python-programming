# defining function to find average of grades
def avg_grade(student):
    sum_of_grade = 0
    # creating a loop for every student
    for stud in student:
        # creating a loop to calculate average
        for grade in stud["grades"]:
            sum_of_grade = sum_of_grade + grade
        print(stud["name"] + ":", format((sum_of_grade/3), ".1f"))
        sum_of_grade = 0


# creating a dictionary with student details
students = [{"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
            {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
            {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
            {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
            {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}]
# calling the function
avg_grade(students)
