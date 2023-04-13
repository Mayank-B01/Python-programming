def detail():
    #defining doc string
    '''this function takes user input for name, age and qualification'''
    #taking user input
    name=input("Enter you name:")
    age=int(input("Enter your age:"))
    qual=input("Enter your qaulification:")
    #displaying output
    print("Name:",name)
    print("Age:",age)
    print("Qualification:",qual)

print(detail.__doc__)
detail()
