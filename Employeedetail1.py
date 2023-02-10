# def getdata():
#     for x in range(10):
#         name = input("\nEnter the Employee details \nEnter your name:") 
#         age = int(input("Enter your age:"))  
#         salary = float(input("Enter your salary:  ")) 
#         display(name,age,salary)

# def display(name,age,salary):
#     for x in range(1):
#         print("Hello ",name,"as your age is",age,"and your salary is",salary,"so we offer u aloan")

# getdata()        




def getdata():
    print("Enter your details\n")
    list1=[]
    for var in range(3):
        name = input("Enter your name: ") # string
        age = int(input("Enter your age: "))  # integer
        salary = float(input("Enter your salary: ")) # float
        list1.append([name,age,salary])
    print(list1)
    display(list1)
def display(LIST1):
    for i in range(3):
        print("Hello ",LIST1[i][0]," as your age is ",LIST1[i][1]," and your salary is ",LIST1[i][2]," so we offer you the loan.")
getdata()

