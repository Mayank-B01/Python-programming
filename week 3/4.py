#defining function to calculate grade percentage
def grade_per(t_score,o_score):
    #calculating grade percentage
    grade=(o_score/m_score)*100
    return grade

#asking user input for five assignments

mark1=float(input("Enter the marks for 1st assignment:"))
mark2=float(input("Enter the marks for 2nd assignment:"))
mark3=float(input("Enter the marks for 3rd assignment:"))
mark4=float(input("Enter the marks for 4th assignment:"))
mark5=float(input("Enter the marks for 5th assignment:"))

#calculating obtained score
o_score=mark1+mark2+mark3+mark4+mark5

#defining max possible score
m_score=500

#calling function
overall_per=grade_per(m_score,o_score)

#printing the result
print("Your overall grade percentage is",overall_per,"%")
