# # # # # a=int(input("Enter the first number"))
# # # # # b=int(input("Enter the second number"))
# # # # # # add=a+b
# # # # # print(add)





# # # # # a=int(input("Enter the first number"))
# # # # # b=int(input("Enter the second number"))
# # # # # add=a+b
# # # # # print(add)

# # # # # a=int(input("Enter the first number"))
# # # # # b=int(input("Enter the second number"))
# # # # # sub=a-b
# # # # # print(sub)



# # # # # a=int(input("Enter the first number"))
# # # # # b=int(input("Enter the second number"))
# # # # # add=a+b
# # # # # print(add)
# # # # # sub=a-b
# # # # # print(sub)










# # # # x=int(input("Enter x value:"))
# # # # y=int(input("Enter y value:"))
# # # # # print(x==y)


# # # x=int(input("Enter x value:"))
# # # y=int(input("Enter y value:"))
# # # print(x==y)
# # # print(x!=y)
# # # print(>)
# # # print(<)
# # # print(>=)
# # # # print(<=)



# # p=True
# # q=False
# # print(p and q)
# # print(p or q)
# # print(not q)
  
# # x=5
# # if x>=15:
# #     print("x is not greaterthan 15")
# # elif x<=15:
# #     print("x is lessthan 15")
# # else

# # tomorrow =input("Enter tomorrows work:")
# # if tomorrow=="work":
# #     print("come to office")
# # elif tomorrow=="outing":
# #     print("go to park")
# # else :
# #     print("stay in home")
    
# age=int(input("Enter yor age"))
# if age>5:
#     print("Free")
# elif age<=5 and age<=12:
#     print("Child Ticket")
# elif age<=13 and age<=59:
#     print("Adult Ticket")
# else:
#     print("Senior Citizen")


# speed=int(input("Enter your speed"))
# if speed<120:
#     print("Overspeed")
# elif speed<=80 and age<=120:
#     print("Fast")
# elif age<=40 and age<=79:
#     print("moderate")
# else:
#     print("Slow")
    
    
# name="Shelplin"
# print(name[::-1])  
# print(name[-3])

# list_stu=["ashika","shelphin","abisha","gayu"]
# print(list_stu[1:3])
# print(list_stu[1:-1])

# email="gayu@gmail.com"
# # username=print(email[0:4])
# # domain=print(email[4:14])
# username,domain=email.split("@")
# print(username)
# print(domain)




# list_stu=["Gayu","Abi","Ashika","Achu"]
# list_stu.append("Appu")
# print(list_stu)
# list_stu.remove("Ashika")
# print(list_stu)
# list_stu[2]="Appu"
# print(list_stu)




# # value={"location":"Manalai","salary":200000,"Dep":"cs"}
# print(value)
# value["location"]="Makadu"
# print(value)
# value.pop("Dep")
# print(value)







# 

# fib=int(input("Enter the number:"))
# f=0
# j=1
# print(f)
# print(j)
# for i in range(2,11):
#     next=f+j
#     print(next)
#     f=j
#     j=next




#
# list=[1,2,3,4,5,4,2]
# result=[]
# for item in  list
#     if item not in result:
#         result.append(item)
#         print(result)





# class Student:
#     def greet(self):
#         print("Hello")
         
#     def student_details(self,name):
#         self.student_name=name
#         print(self.student_name)
          
# stu=Student()
# stu.greet()
# stu.student_details("vini")




#


# class Student:
#     def greet(self):
#         print("Hello")
#     def student_details(self,name):
#         print(f"Name:{name}")
#         self.name=name
        
#     def bye(self):
#         print(f"bye bye{self.name}")
         
         

# student1=Student()
# student1.greet()
# student1.student_details("shiji")
# student1.bye()



# student2=Student()
# student2.greet()
# student2.student_details("Godwin")
# student2.bye()







#

# def__init__(self,username):
#     self.username=username
 
# def print_username(self):
#     print(self.username)
# def print_welcome_massege








# import random

# choices = ["rock", "paper", "scissors"]

# computer = random.choice(choices)

# user = input("Enter rock, paper, or scissors: ").lower()

# print("Computer chose:", computer)

# if user not in choices:
#     print("Invalid choice!")
# elif user == computer:
#     print("It's a tie!")
# elif (user == "rock" and computer == "scissors") or \
#      (user == "paper" and computer == "rock") or \
#      (user == "scissors" and computer == "paper"):
#     print("You win!")
# else:
#     print("Computer wins!")










# Simple Calculator

# 







# Calculator using functions


#     if b == 0:
#         return "Cannodef add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):t divide by zero"
#     return a / b

# # Input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Choose an operation (1/2/3/4): ")

# if choice == '1':
#     print("Result =", add(num1, num2))
# elif choice == '2':
#     print("Result =", subtract(num1, num2))
# elif choice == '3':
#     print("Result =", multiply(num1, num2))
# elif choice == '4':
#     print("Result =", divide(num1, num2))
# else:
#     print("Invalid choice")





 



# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")










#include <stdio.h>

# 










# num = int(input("Enter a number: "))

# if -9 <= num <= 9:
#     print("Single-digit number")
# else:
#     print("Multi-digit number")