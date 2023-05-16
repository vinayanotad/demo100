# def getdata(name,age,salary):
#     print("Enter the details\n")
#     name = input("Enter your name:") 
#     age = int(input("Enter your age:"))  
#     salary = float(input("Enter your salary: ")) 

#
# def config():
#     for (e==0,e<10,e++)
#     getdata(name,age,salary)
#     display()

# def display():
#     e=employee("name",name,"age",age,"salary",salary)

# config()


#BUBBLE SORT 

List1 = []

n = int(input("Enter the n value: "))

print("Enter the elements: ")
for i in range(n):
    List1.append(int(input()))

for i in range(0,n-2):
    for j in range(1,n):
        if(List1[i] > List1[j]):
            temp = List1[i]         # temp = 10
            List1[i]=List1[j]       # 10=30
            List1[j]=temp           # 30=temp
            print(List1,end=" | ")