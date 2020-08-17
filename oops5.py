# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:38:11 2020

@author: HASSAN ENTERPRISES
"""
class Complex:
# defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i
# overloading the add operator using special function
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return complex(r,i)
# string function to print object of Complex class
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'
c1 = Complex(5,3)
c2 = Complex(2,4)
print("sum = ",c1+c2)
#--------------------------------------------------------------------------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y) 
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return(x,y)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
p1 = Point(5, 4)
p2 = Point(4, 2)
#print(p1.point())
print(p1-p2)
print(p1+p2)
#---------------------------------------------------------------------------------------------
x=5
y=8
print(int.__add__(x,y))
#------------------------------------------------------------------------------------------------
class fruit:
    pass
class Apple(fruit):
    def type(self):
        return("I am  apple")
    def color(self):
        return("My color is red")
class Mango(fruit):
    def type(self):
        return("I am manago")
    def color(self):
        return("my color is yellow")
AP=Apple()
MG=Mango()
for fruits in (AP,MG):
    fruits.type()
    fruits.color()    
#------------------------------------------------------------------------------------------
from abc import ABCMeta,abstractmethod 
class Vehicle(metaclass=ABCMeta):
    def model(self):
        pass
    def color(self):
        pass
class Bike(Vehicle):
    def model(self):
        return("Its Model is 70")
    def color(self):
        return("It color is black")
class Car(Vehicle):
    def model(self):
        return("Its model is 2019")
    def color(self):
        return("Its color is white")
BI=Bike()
CR=Car()
for vehicles in (BI,CR):
    print(vehicles.model())
    print(vehicles.color())
#------------------------------------------------------------------------------------------------
list=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter the number you want to knbow the table"))
for i in list:
    c=n*i
    print("The table of that number is", c)
#-------------------------------------------------------------------------------------------------

    
def table(n,u):
    #n=int(input("enter the number which you want to fingd trhe table : "))
    for i in u:
        c=n*i
        print(c)
n=int(input("enter the number which you want to fingd trhe table : "))    
table(n,[1,2,3,4,5,6,7,8,9,10])    
#n=int(input("enter the number which you want to fingd trhe table : "))    
#---------------------------------------------------------------------------------------------------
class Distance:
    def __init__(self,i,f):
        self.inches=i
        self.feet=f
    def __add__(self,other):
        i=self.inches + other.inches
        f=self.feet + other.feet
        return ("The total inches is {0} and total feet is {1}".format(i,f))
d1=Distance(3,4)
d2=Distance(6,7)
print(" {}".format(d1+d2))    
#---------------------------------------------------------------------------------------------------------
class Time:
    def __init__(self,h,m,s):
        self.hours=h
        self.minutes=m
        self.second=s
    def __sub__(self,other):
        h=self.hours-other.hours
        m=self.minutes-other.minutes
        s=self.second-other.second
        return("The current time is {} hours  {} minutes and  {} seconds".format(h,m,s))
t1=Time(5,6,7) 
t2=Time(3,2,1)
print(t1-t2) 
#----------------------------------------------------------------------------------------------------------  
# question 1:
from abc import ABC, abstractmethod
class NetworkInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def transfer(self):
        pass
class RealNetwork(NetworkInterface):
    def connect(self):
        print("Network is connect")
    def transfer(self):
        print("All Data is tranfser")
R1= RealNetwork()
R1.connect()
R1.transfer()
#--------------------------------------------------------------------------------------------
#question 2
from abc import ABC, abstractmethod
class NetworkInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def transfer(self):
        pass
class RealNetwork(NetworkInterface):
    def connect(self):
        print("Network is connect")
    def transfer(self):
        print("All Data is tranfser")
class FakeNetwork(NetworkInterface):
    def connect(self):
        print("Network is connect")
R1= RealNetwork()
R1.connect()
R1.transfer()
F1= FakeNetwork()
F1.connect()
#-----------------------------------------------------------------------------------------------
#question 3:
class A:
# defining init method for class
    def __init__(self, x,y):
        self.x = x
        self.y = y
# overloading the add operator using special function
    def __add__(self, other):
        x = self.x + other.y
        y = self.x + other.y #2+
        return( x,y)
    
c1 = A(5,3)
c2 = A(2,3)
print("sum = ",c1+c2)
#-----------------------------------------------------------------------------------------------
#question 4:
class A:
# defining init method for class
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        if self.x < other.y:
            return True
        else:
            return False
class B:
# defining init method for class
    def __init__(self, y):
        self.y = y
c1 = A(2)
c2 = B(4)
print("Is c1 less than c2: ",c1<c2)
#------------------------------------------------------------------------------------------------
class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob3 == ob4)        
#-----------------------------------------------------------------------------------------------
class A:
# defining init method for class
    def __init__(self, x):
        self.x = x
class B:
# defining init method for class
    def __init__(self, y):
        self.y = y        
class C(A,B):
    
            
    def __lt__(self, other):
        if self.x < other.y:
            return True
        else:
            return False   
c1 = C(2)
c2 = C(4)
print("Is c1 less than c2: ",c1<c2)  

#-------------------------------------------------------------------------------------------------
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        x=self.x+other.y
        y=self.x+other.y
        return(x,y)
    def __sub__(self,other):
        x=self.x-other.y
        y=self.x-other.y
        return(x,y)
    def __gt__(self,other):
       
        x=self.x>other.y
        y=self.x>other.y
        if x and y:
             return(True)
        else:
            return(False)
    def __lt__(self,other):
       
        x=self.x<other.y
        y=self.x<other.y
        if x and y:
             return(True)
        else:
            return(False)
    def __ge__(self,other):
       
        x=self.x>=other.y
        y=self.x>=other.y
        if x >= y:
             return(True)
        else:
            return(False) 
    def __le__(self,other):
       
        x=self.x<=other.y
        y=self.x<=other.y
        if x <= y:
             return(True)
        else:
            return(False)     
    def __eq__(self,other):
       
        x=self.x==other.y
        y=self.x==other.y
        if x == y:
             return("Both are equal")
        else:
            return("Both are not equal")     
    

c1=Point(2,3)
c2=Point(4,5)
print("The sum is ",c1+c2)
print("the Subtraction is ",c1-c2)
print("The C1 is greater than C2",c1>c2)
print("The C1 is less than C2",c1<c2)
print("the C1 is greater than or equal to c2",c1>=c2)
print("the C1 is less than or equal to c2",c1<=c2)
print("the C1 is  equal to c2",c1==c2)
#---------------------------------------------------------------------------------------------------------------

import re
string = "Python is fun"
# check if 'Python' is at the beginning
match = re.search('fun$', string)
if match:
    print("pattern found inside the string")
else:
    print("pattern not found")    
    
    
    
#--------------------------------------------------------------------------------------------------
import re
str = " The rain in Spain"
x = re.findall("Sp", str)
print(x)        
#---------------------------------------------------------------------------------------------------
import re
str = " The rain in Spain"
x = re.findall("in", str)
print(x)    
#-------------------------------------------------------------------------------------------------
import re
str = " The rain in Spain"
x = re.findall("i", str)
print(x)    
#---------------------------------------------------------------------------------------------------
import re
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)
#---------------------------------------------------------------------------------------------------
import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)
#-----------------------------------------------------------------------------------------------------
import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\s'
result = re.split(pattern, string)
print(result)
#--------------------------------------------------------------------------------------------------------
import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\t'
result = re.split(pattern, string)
print(result)
#----------------------------------------------------------------------------------------------------------
import re
# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)
#----------------------------------------------------------------------------------------------------------
import re
# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\d+\s+'
# empty string
replace = 'aaa'
new_string = re.sub(pattern, replace, string)
print(new_string)

#-----------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
class FourWheelVehicle (ABC):
    @abstractmethod
    def SpeedUp(self):
        pass
   
class Car(FourWheelVehicle):
    def SpeedUp(self):
        print(" Running! ")
class TwoWheelVehicle (ABC):
    @abstractmethod
    def SpeedUp(self):
        pass         

class Bike(TwoWheelVehicle):
    def SpeedUp(self) :
        print(" Running!.. ")
a = Bike ()
s = Car()
print( isinstance(s, FourWheelVehicle))
print( isinstance(s, TwoWheelVehicle))
print( isinstance(a, FourWheelVehicle))
print( isinstance(a, TwoWheelVehicle))
#------------------------------------------------------------------------------------------------------------



from abc import ABC, abstractmethod
class shape(ABC):
    def Area(self):
        pass
class Square(shape):
    def __init__(self,side):
        self.side=side
    def Area(self):
        Area=int(self.side)*int(self.side)
        return("The Area Of Square is {}".format(Area))
class Triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def Area(self):
        Area=1/2*(int(self.base)*int(self.height))
        return ("The Area Of triangle is   {}".format(Area))
Sq=Square("4")
Tr=Triangle("5","2" )
for i in(Sq,Tr):
    print(i.Area())
#---------------------------------------------------------------------------------------------------------------
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_Salary(self):
        return(self.pay*12)+self.bonus
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.instance_Object=Salary(pay,bonus)
    def Total_Salary(self):
        return(self.instance_Object.annual_Salary())
emp=Employee("max",25,15000,10000)    
print(emp.Total_Salary())
#-------------------------------------------------------------------------------------------------------------    

#Association Example Aggregation has a relation (In association no class depend with each other if one is dies so its does not effect on other classs)
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_Salary(self):
        return(self.pay*12)+self.bonus
class Employee:
    def __init__(self,name,age,salaray):
        self.name=name
        self.age=age
        self.instance_Object=salaray
    def Total_Salary(self):
        return(self.instance_Object.annual_Salary())
salaray=Salary(15000,10000)    
emp=Employee("max",25,salaray)    
print(emp.Total_Salary())




#---------------------------------------------------------------------------------------------------------------
class Birthday:
    def __init__(self,Day,Month,Year):
        self.Day=Day
        self.Month=Month
        self.Year=Year
    def dateOfbirth(self):
        return("My date of birth is {0}/{1}/{2} and I am resident of Karachi".format( self.Day,self.Month,self.Year))
class Person:
    def __init__(self,name,age,CNICNumber,Day,Month,Year):
        self.name=name
        self.age=age
        self.CNICNumber=CNICNumber
        #self.Day=Day
        #self.Month=Month
        #self.Year=Year
        self.instance_Object=Birthday(Day,Month,Year)
    def PrintDetails(self):
        return("My name is {} and my age is {} my CNIC number is {} ".format(self.name, self.age,self.CNICNumber)+"and "+(self.instance_Object.dateOfbirth()))

Pr=Person("Muhammad Huzaifa",20,3465756868669,15,11,1999)  
print(Pr.PrintDetails())     
#-----------------------------------------------------------------------------------------------------------------------




import re
file=open("New Text Document.txt","r")
f=file.read()
b=f.split()
a=[]
a.append(b)
pattern1=("033")
ufone=re.findall(pattern1,f)
pattern2=("030")
Mobilink=re.findall(pattern2,f)
pattern3=("031")
Zong=re.findall(pattern3,f)
pattern4=("032")
Warid=re.findall(pattern4,f)
pattern5=("032")
Telenor=re.findall(pattern5,f)
#print(len(ufone))
#print(a)

for i in a:
   for j in range(len(i)):
       #print(i[0])
       k=(i[j][0:4])
       #---------------------Ufone---------------------------------------------------
       match1=re.search("^0336",k) 
       match2=re.search("^0335",k)
       match3=re.search("^0334",k)
       match4=re.search("^0337",k)
       match5=re.search("^0333",k)
       match6=re.search("^0332",k)
       match7=re.search("^0331",k)
       #------------------------- Warid------------------------------------------------
       match8=re.search("^0320",k)
       match9=re.search("^0321",k)
       match10=re.search("^0322",k)
       match11=re.search("^0323",k)
       match12=re.search("^ 0324",k)
       match13=re.search("^0325",k)
       #------------------------Zong----------------------------------------------------
       match14=re.search("^0310",k)
       match15=re.search("^0311",k)
       match16=re.search("^0312",k)
       match17=re.search("^0313",k)
       match18=re.search("^0314",k)
       match19=re.search("^0315",k)
       #---------------------Telenor----------------------------------------------------
       #0340, 0341, 0342, 0343, 0344, 0345, 0346, 0347
       match20=re.search("^0340",k)
       match21=re.search("^0341",k)
       match22=re.search("^0342",k)
       match23=re.search("^0343",k)
       match24=re.search("^0344",k)
       match25=re.search("^0345",k)
       match26=re.search("^0346",k)
       match27=re.search("^0347",k)
       #--------------------- SCOM-------------------------------------------------------
       match28=re.search("^0335",k)
       #----------------------Instaphone-------------------------------------------------
       match29=re.search("^0364",k)
       #----------------------Mobilink----------------------------------------------------
       #0300, 0301, 0302, 0303, 0304, 0305, 0306, 0307,0308, 0309, 03000
       match30=re.search("^0300",k)
       match31=re.search("^0301",k)
       match32=re.search("^0302",k)
       match33=re.search("^0303",k)
       match34=re.search("^0304",k)
       match35=re.search("^0305",k)
       match36=re.search("^0306",k)
       match37=re.search("^0307",k)
       match38=re.search("^0308",k)
       match39=re.search("^0309",k)
       match40=re.search("^0300",k)

       if (match1 or match2 or match3 or match4 or match5 or match6 or match7 ):
           print("The Network is  Ufones  and Number is " + i[j])
           
       elif ( match8 or match9 or match10 or  match11 or match12 or  match13):
           print("The Network is  Warid and Number is " + i[j]) 
       elif ( match14 or match15 or match16 or match17 or match18 or match19 ):
           print("The Network is  Zong and Number is  " + i[j]) 
       elif ( match20 or match21 or match22 or match23 or match24 or match25 or match26 or match27):
           print("The Network  is Telenor and Number is " + i[j])
       elif ( match28):
           print("The Network is SCOM and Number is " + i[j]+ "AJK & Gilgit- Baltistan")    
       elif(match29):
           print("The Network is  Instaphone and Number is " + i[j])
    
       elif(match30 or match31 or match32 or match33 or match34 or match35 or match36 or match37 or match38 or match39 or match40):
           print("The Number is Mobilink " + i[j])
       else:
           print("The number  is Wrong !")
           
print("The total Number of Ufone user is {}".format(len(ufone)))
print("The total Number of  Mobilink user is {}".format(len(Mobilink)))
print("The total Number of  Warid user is {}".format(len(Warid)))
print("The total Number of  Zong user is {}".format(len(Zong)))
print("The total Number of  Telenor user is {}".format(len(Telenor)))
#-----------------------------------------------------------------------------------------------------------
class Box:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def __mul__(self,other):
        global box1,box2
        box1=self.length*self.breadth
        box2=other.length*other.breadth
        return(box1,box2)
    def __lt__(self,other):
        Box1=self.length*self.breadth
        Box2=other.length*other.breadth
        if(Box1<Box2):
            return("Box1 is less than Box2")
        else:
            return("Box1 is not less than box2")
    def Area_of_Box(self):
        return("The Area of Box1 is {} and the Area of box2 is {}".format(box1,box2))
   
Box1=Box(43,5)
Box2=Box(89,4)
print(Box1*Box2)
print(Box1<Box2)
print(Box1.Area_of_Box())

#------------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self,EmployeeName,EmployeeId):
        self.EmployeeName=EmployeeName
        self.EmployeeId=EmployeeId
    def set_EmployeeId(self,EmployeeId):
        global x
        x=EmployeeId
        self.EmployeeId=x
   
    def set_EmployeeName(self,EmployeeName):
        self.EmployeeName=EmployeeName
    def get_EmployeeName(self):
        return(self.EmployeeName,x) 
Employee1=Employee("Muhammad huzaifa",12344)
Employee1.set_EmployeeId(12344)
print(Employee1.get_EmployeeName())   
Employee2=Employee("Muhammad bilal",34566)
print(Employee2.get_EmployeeName())
Employee3=Employee("saad",45576786)
print(Employee3.get_EmployeeName())
#---------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self,EmployeeName,EmployeeIdd):
        self.EmployeeName=EmployeeName
        self.EmployeeIdd=EmployeeIdd
    def set_EmployeeName(self,EmployeeName):
        self.EmployeeName=EmployeeName
       
    def set_EmployeeId(self,EmployeeId):
        global x
        x=EmployeeId
        self.EmployeeId=x
    def get_EmployeeName(self):
        return("The Employee Name is {} and its Id is {}".format(self.EmployeeName,x))     
    
    name=property(get_EmployeeName,set_EmployeeName)
    Id=property(set_EmployeeId)
Employee1=Employee("Muhammad",12344)
Employee1.EmployeeId=12344
print(Employee1.name)
Employee2=Employee("bilal",34567)
print(Employee2.name)
Employee3=Employee("Hamza",34567)
print(Employee3.name)             
#---------------------------------------------------------------------------------------------------------------
import sys
class Student:
    def __init__(self,RollNumber,Department):
        self.RollNumber=RollNumber
        self.Department=Department
    def set_RollNumber(self,RollNumber):
        self.RollNumber=RollNumber
    def get_RollNumber(self):
        return("Rollnumber is {}".format(self.RollNumber))
    def set_Department(self,Department):
        self.Department=Department
    def get_Department(self):
        return("Department is {}".format(self.Department))
    def GetInformation(self,Student):
        global x,y,z
        z=Student
        x=self.RollNumber
        y=self.Department
    def DisplayInformation(self):
        self.GetInformation(StudentName)
        return("The Student Name is {} RollNumber of student is {} and belong to this {} Department".format(z,x,y)) 
#StudentName=input("Enter the Student Name")
#Rollnumber=input("Enter the Student RollNumber")
#Department=input("Enter the Student Department")       
#Stu=Student(Rollnumber,Department)
#print(Stu.DisplayInformation()) 
#Stu.set_RollNumber("19B-136-Cs")
#Stu.set_Department("Software Engineering")
#print(Stu.DisplayInformation())       
class Employee:
    def __init__(self,EmployeeNumber,EmployeeSalary):
        self.EmployeeNumber=EmployeeNumber
        self.EmployeeSalary=EmployeeSalary
    def  set_EmployeeNumber(self,EmployeeNumber):
        self.EmployeeNumber=EmployeeNumber
    def set_EmployeeSalary(self,EmployeeSalary):
        self.EmployeeSalary=EmployeeSalary
    def get_EmployeeNumber(self):
        return("The Employee Number is {}".format(self.EmployeeNumber))
    def get_EmployeeSalary(self):
        return("The Salary of Employee is {}".format(self.EmployeeSalary))
    def GetInformation(self,Employee):
        global  x,y,z
        z=Employee
        x=self.EmployeeNumber
        y=self.EmployeeSalary
    def  DisplayInformation(self):
        self.GetInformation(EmployeeName)
        return("The Employee Name is {} and Employee Number is {} and it has a Salary of Rs {}/=".format(z,x,y))
#EmployeeName=input("Enter the Employee Name  ")
#Employee_Number=input("Enter the Employee Number ")
#Employee_Salary=input("Enter the Employee Salary ") 
#Emp=Employee(Employee_Number,Employee_Salary)
#print(Emp.DisplayInformation())        

class TeachingAssistant(Student,Employee):
    def __init__(self,timing,RollNumber,Department,EmployeeNumber,EmployeeSalary):
        Student.__init__(self,RollNumber,Department)
        Employee.__init__(self,EmployeeNumber,EmployeeSalary)
        self.timing=timing
    def set_timing(self,timing):
        self.timing=timing
    def get_timing(self):
        return("The new timing is {}".format(self.timing))
    def GetInformation(self):
        while(True):
            print("What Information You want To Get Student Or Employee")
            print("1) Student Information")
            print("2) Employee Information")
            print("3) Quit")
            user_choice=input()
            if user_choice not in ["1","2","3"]:
                print("Please enter a Valid Option")
                continue
           
            else:
                user_choice=int(user_choice)        
                if user_choice ==1:
                    Stu=Student(Rollnumber,Department)
                    print(Stu.DisplayInformation())
                    print("Do you want to Set the Student Data say Yes or No")
                    user_choice=input("Enter your Answer")
                    if user_choice=="Yes":
                        x=input("Enter the RollNumber")
                        y=input("Enter the Department")
                        Stu.set_RollNumber(x)
                        Stu.set_Department(y)
                        print(Stu.DisplayInformation())
                        print("The Timing is {}".format(self.timing))
                    elif user_choice =="No":
                         Stu=Student(Rollnumber,Department)
                         print(Stu.DisplayInformation())
                         print("The Timing is {}".format(self.timing))
                    else:
                        sys.exit(0)
                        
                elif user_choice==2:
                    Emp=Employee(Employee_Number,Employee_Salary)
                    print(Emp.DisplayInformation()) 
                    print("Do you want to Set the Employee Data say Yes or No")
                    user_choice=input("Enter your Answer")
                    if user_choice=="Yes":
                        x=input("Enter the EmployeeNumber")
                        y=input("Enter the Employee Salary")
                        Emp.set_EmployeeNumber(x)
                        Emp.set_EmployeeSalary(y)
                        
                        print(Emp.DisplayInformation())
                        print("The teaching assistant timing is  {}".format(self.timing))
                    elif user_choice =="No":
                        Emp=Employee(Employee_Number,Employee_Salary)
                        print(Emp.DisplayInformation())
                        print("The teaching assistant timing is {}".format(self.timing))
                else:
                    sys.exit(0)
                
        
    def DisplayInformation(self):
        print("Do you want to see Student Information or Employee Information")
        print("Press c to continue and q to exit") 
        user_choice2=""
        while(user_choice2 !="c"and user_choice2 !="q"):
            user_choice2=input()
            if user_choice2=="q":
                sys.exit()
            if user_choice2 =="c":
                 
                self.GetInformation()
        
        
StudentName=input("Enter the Student Name")
Rollnumber=input("Enter the Student RollNumber")
Department=input("Enter the Student Department") 
EmployeeName=input("Enter the Employee Name  ")
Employee_Number=input("Enter the Employee Number ")
Employee_Salary=input("Enter the Employee Salary ")
    
TA=TeachingAssistant("12:30",Rollnumber,Department,Employee_Number,Employee_Salary)
print(TA.DisplayInformation())    
                     