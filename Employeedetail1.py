def getdata():
    for x in range(10):
        name = input("\nEnter the Employee details \nEnter your name:") 
        age = int(input("Enter your age:"))  
        salary = float(input("Enter your salary:  ")) 
        display(name,age,salary)

def display(name,age,salary):
    for x in range(1):
        print("Hello ",name,"as your age is",age,"and your salary is",salary,"so we offer u aloan")

getdata()        