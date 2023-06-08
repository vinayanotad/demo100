def getdata():
    count=0
    while(count<10):
        count=count+1
        name = input("\n Enter the details of Employee \nEnter your name:") 
        age = int(input("Enter your age :"))  
        salary = float(input("Enter your salary:  ")) 
        display(name,age,salary)
        
def display(name,age,salary):
    count=0
    while(count<1):
        count=count+1
        print("Hello ",name,"as your age is",age,"and your salary is",salary,"so we offer u aloan")
        
getdata()




            
