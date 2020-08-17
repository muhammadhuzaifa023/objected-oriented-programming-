# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:35:06 2020

@author: HASSAN ENTERPRISES
"""


data=("Muhammad Huzaifa","20")
print(data)
data[1:3]
class Person:
    def __init__(self,fathername,myname,age,gender):
        self.fathername=fathername
        self.myname=myname
        self.age=age
        self.gender=gender
pr=Person("Muhammad Sohail","Muhmmad Huzaifa","20","Male")
print(pr.fathername)
print(pr.gender)
#----------------------------------------------------------------------------------------------------------
try:
   a=10
   b=5
   print(a//b)
except:
   print('Some error occurred.')
print("Out of try except blocks.")
#------------------------------------------------------------------------------------------------------------
try:
    a=10
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")
#---------------------------------------------------------------------------------------------------------
try:
    a=5
    b='0'
    print (a+b)
except TypeError:
    print('int and string cannot concenate with each other')
print ("Out of try except blocks")
#-----------------------------------------------------------------------------------------------------------
try:
    a=5
    b="0"
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')
#-----------------------------------------------------------------------------------------------------------
try:
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print(" Wait")
    print("finally block")
print ("Out of try, except, else and finally blocks." )    
#----------------------------------------------------------------------------------------------------------------
try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")        
#----------------------------------------------------------------------------------------------------------------
import math
while(True):
    print("Sir what you want to calculate")
    print("1) quadritic Formula")
    print("2) Distance Formula")
    
    user_choice=input("Enter the values 1 or 2  ")
    if user_choice not in ["1","2"]:
            print("Please enter a Valid Option")
            continue
    else:
         user_choice=int(user_choice)
    if user_choice ==1:
        print("Please Enter the values")
        a=int(input("Enter the value a "))
        b=int(input("Enter the value b "))
        c=int(input("Enter the value c "))
        if (a=="" or b=="" or c==""):
            print("Please enter the Value ")
        else:
            try:
                x=-b+(math.sqrt(b**-4*a*c))
                y=x/2
                z=y/a
                
                d=-b-(math.sqrt(b**-4*a*c))
                e=d/2
                f=e/a
            except ZeroDivisionError:
                print("Division by zero is not  possible")
            else:
                print("The answer is {} and {}".format(z,f))
    elif user_choice ==2: 
        print("Please Enter the Values")
        x1=int(input("enter the Value X1 "))
        x2=int(input("enter the value X2 "))
        y1=int(input("enter the Value y1 "))
        y2=int(input("enter the value y2 "))
        if (x1=="" or x2=="" or y1=="" or y2==""):
            print("Please enter the Value ")
        else:
            try:
                x=math.sqrt((x2**2-x1**2)+(y2**2-y1**2))
                
            except ValueError: 
                print("Please Enter the Numeric Number Not word")
            else:
                print("The answer is {}".format(x))
                       
    