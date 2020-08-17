# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:54:44 2020

@author: HASSAN ENTERPRISES
"""
#Question 2 part a:
class data:
    def __init__(self,distance,time):
        self.distance=distance
        self.time=time
    def formula(self):
        v=self.distance//self.time
        return("velocity={}m/s".format(v))
f1=data(100,4)
print(f1.formula())        
#---------------------------------------------------------------------------
#Question 2 part b:
import math
class data:
    def __init__(self,velocity_of_sailboat,velocity_of_water):
        self.s=velocity_of_sailboat
        self.w=velocity_of_water
    def formula(self):
        
        x=math.sqrt(self.s**2+self.w**2)
        return("velocity={}km/h".format(x))
f2=data(10,5) 
print(f2.formula())  
#---------------------------------------------------------------------------     
import math
class data:
    def __init__(self,Vw,Vb):
        self.velocity_of_water=Vw
        self.velocity_of_boart=Vb        
    def Velocity(self):
        vb=self.velocity_of_boart*1000//3600
        vw=self.velocity_of_water*1000//3600
        V=math.sqrt(vb**2+vw**2)
        return("The velocity of water is={}m/s".format(V))
    def Angle(self):
        Ag=math.atan(self.velocity_of_boart//self.velocity_of_water)
        return("The angle Formed between boart and water is={}".format(Ag))

F1=data(5,10)
print(F1.Velocity())
print(F1.Angle())

#Question 3 part d:
#hours=2hours:3min:38sec
class data:
    def __init__(self,distance,hours,min,sec):
        self.distance=distance
        self.hours=hours
        self.min=min
        self.sec=sec
    def formula(self):
        x=self.distance*100
        time=self.hours*60*60+self.min*60+self.sec
        v=x//time
        return("velocity={}m/s".format(v))
f3=data(42.195,2,3,38)
print(f3.formula())        

#===================================================================================================
class point:
    pass
p1=point()
p2=point()
p1.x=5
p2.y=6
p3=point()
p4=point()
p5=point()
print(p1.x,p2.y)
p3.u=7
p4.w=8
p5.v=9
print(p3.u,p4.w,p5.v)
#=================================================================================================
class point2:
    def reset(self):
        self.x=0
        self.y=0
p3=point2()
p3.u=56
p3.v=89
print(p3.reset())
p3.w=45
print(p3.u,p3.v,p3.w)
p3.reset()
p3.x=87
p3.y=98
p3.z=67
print(p3.x,p3.y,p3.z)  
#==========================alternate method=============================================================
class point3:
    def reset(self):
        self.x=0
        self.y=0
p4=point3()
p4.x=34
p4.y=45
print(p4.x,p4.y)
(point3.reset(p4))
#=====================================================================================

class Point4:
    def move(self,x,y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0)
    def Calculate_distance(self,other_points):
        return math.sqrt((self.x-other_points)**2+
                         (self.y-other_points)**2)
p6=Point4()
p7=Point4()
p6.reset()
p7.move(5,0)
print(p7.Calculate_distance(p6))    
p6.move(3,4)
print(p6.Calculate_distance(p7))
#here assert used as a bool it check the value whether itnis true or false 
assert (p6.Calculate_distance(p7))==(p7.Calculate_distance(p6))
#===========================================================================================
class initial_velocity:
    def __init__(self,vf,a,t):
        self.final_velocity=vf
        self.acceleration=a
        self.time=t
    def formula(self):
        vi=self.final_velocity-self.acceleration*self.time
        return("initial_velocity={}m/s".format(vi))
f1=initial_velocity(5,10,3)
print(f1.formula())        
#=============================================================================================
class Employee:
    pass
#making a object which represent class template ka 
huzaifa=Employee()
bilal=Employee()
huzaifa.fname="Mohammad"
huzaifa.lname="Huzaifa"
huzaifa.salary="44000"
bilal.fname="Mohammad"
bilal.lname="Bilal"
bilal.salary="34000"
x=huzaifa.fname+huzaifa.lname
y=bilal.fname+bilal.lname
print("fullName:{} and salary of huzaifa is={}".format(x,huzaifa.salary))
print("fullName:{} and salary of bilal is={}".format(x,bilal.salary))
#========================================================================================================
#--------------making a class vriable-----------------------------------------------------------------
class employee:
    salary=1.5 #this is class variable which can access by 
    def __init__(self,fname,lname,salary):
        self.fname=fname # self.fname is a instance variable its a variable of constructor
        self.lname=lname
        self.salary=salary
        
    def increment(self):
        x=self.salary*employee.salary # class vaiable can be share by both because it a variable of class 
        y=self.fname+self.lname
        return ("{} has a incremented salary is {}".format(y,x))
h1=employee("Mohammad","Huzaifa",4400)
print(h1.increment())
print(h1.salary)

h2=employee("Mohammad","Bilal",230000)
print(h2.increment())
#---------------------------------------------------------------------------------------------------------------
#if we want to show how many instace variable are there soo we use __dict__
print(h1.__dict__)
# if I want to show how many variable in class soo we use 
print(employee.__dict__)
#=============================================================================================================
a="PL"
a*3
a
#==============================================================================================================
#if i want to change class variable too may use krayooga decroater class dectoratos
class employee:
    increment=1.5 # class variable hai ya ek joo class say bhi exceess kiya jasakta haoo or instance say bhii excess kiya jasakta haoo
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        x=self.salary*self.increment
        return(x)    
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
        
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
print(h1.increase())
employee.change_increment(4)
print(h1.increase())
print(h2.increase())        
#================================================================================================================
class pratice:
    vi_t=10
    s_t=5
    def __init__(self,vf,e):
        self.final_velocity=vf
        self.acceleration=e
    def initial_velocity_dISTANCE_ACCELERATION(self):
        global vi
        vi=self.final_velocity-self.acceleration*self.vi_t
        return("initial velocity is={}".format(vi))
    def Distance(self):
        global vi,S
        
        
        S=vi*self.s_t+0.5*self.acceleration*self.s_t
        return("Distance is ={}".format(S))
    def Acceleration(self):
        global S 
        a=self.final_velocity**2-vi**2//2*S    
        return("Acceleration is={}".format(a))
        
    @classmethod
    def changing_value(cls,viamount,stamount):
        cls.vi_t=viamount
        cls.s_t=stamount

h1=pratice(100,5)
print(h1.initial_velocity_dISTANCE_ACCELERATION())
print(h1.Distance())
print(h1.Acceleration())
pratice.changing_value(4,6)
print(h1.initial_velocity_dISTANCE_ACCELERATION())
print(h1.Acceleration())
print(h1.Distance())
#==================================================================================================
# Making a classmethod as alternate constructor :
#if i want to change class variable too may use krayooga decroater class dectoratos
class employee:
    increment=1.5 # class variable hai ya ek joo class say bhi exceess kiya jasakta haoo or instance say bhii excess kiya jasakta haoo
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        x=self.salary*self.increment
        return(x)    
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
    @classmethod # as a alterntive constructor
    def from_string(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls( fname,lname,salary)

    
        
lovish=employee.from_string("Mohammad-Huzaifa-440000")        
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
print(h1.increase())
employee.change_increment(4)
print(h1.increase())
print(h2.increase())        
print(lovish.fname)
print(lovish.lname)
print(lovish.salary)

#---------------------------------------------------------------------------------------------------------
# Making a static method which  here use as a decorator yahan hum esliya use kertay hai ka humay aghr class ka variable
 #ko argument nh dy naaa hiii constructor koo margument dyna haoiiii too hum eskaliya use kertay haiiiii 
class employee:
    increment=1.5 # class variable hai ya ek joo class say bhi exceess kiya jasakta haoo or instance say bhii excess kiya jasakta haoo
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        x=self.salary*self.increment
        return(x)    
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
    @classmethod # as a alterntive constructor
    def from_string(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls( fname,lname,salary)
    @staticmethod
    def office_open_closed(day):
        if day=="sunday":
            print("true")
        else:
            print("false")
        
        

    
print(employee.office_open_closed("Monday"))
print(h1.office_open_closed("sunday"))       
lovish=employee.from_string("Mohammad-Huzaifa-440000")        
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
print(h1.increase())
employee.change_increment(4)
h1.change_increment(3)
print(h1.increase())
print(h2.increase())        
print(lovish.fname)
print(lovish.lname)
print(lovish.salary)
#================================================================================================
# using inheritance property 
# what is inheritance property why we use it ?
#from inheritance we can excess the other class attributes in its parent class or child class example
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        print(self.salary)
        print(self.fname)
        print(self.lname)
class programmer(employee):#yahan pr programmer ek dusarii class haii joo inherit haii upper walii class say likin 
    #eska oject ki help say may nay upper wali class ka attributes koo call kiyaaa
    pass        
h1=employee("Mohammad","Huzaifa",440000)
print(h1.increase())        
h2=programmer("Mohammad","Bilal",340000)
print(h2.fname)
print(h2.lname)
print(h2.salary)

# aghr may upper walay constructor use kerna chata hoo or ya chata hoo ka dooobhara nh likhayoo ya wohii doobhara call
# call hojaya too may super().__init__() ka use krayooga joo mujhy wohiii upper waly constructor koo call kerka dy dygaaa
# example:::
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        print(self.salary)
        print(self.fname)
        print(self.lname)
class programmer(employee):#yahan pr programmer ek dusarii class haii joo inherit haii upper walii class say likin 
    #eska oject ki help say may nay upper wali class ka attributes koo call kiyaaa
    def __init__(self,fname,lname,salary,prolang,exp):
        super().__init__(fname,lname,salary)
        self.prolang=prolang
        self.experience=exp
h1=employee("Mohammad","Huzaifa",440000)
print(h1.increase())        
#h2=programmer("Mohammad","Bilal",340000)
#print(h2.fname)
#print(h2.lname)
h1=programmer("Mohammad","Huzaifa",440000,"python","5-Year")
print(h1.prolang)
print(h1.experience)
print(help(programmer))
#==============================================================================================
# using Magic Method or we dunder methods kiya hootay haiiii
#example of dunder method in python it is builtin function in python 
print(4+6)
print("Mohammad"+"Huzaifa")
#bukul esii thera python may dunder methods bhiii hotay haiiiiii
a=6
print(a.__add__(7))
a=6
print(a.__bool__())
a=7
print(a.__mul__(7))
z=7
print(z.__mod__(7))
q=4
print(q.__divmod__(3))
#================================================================================================
class employee:
    def __init__(self,fname,lname,salary):
         self.fname=fname
         self.lname=lname
         self.salary=salary
    def increase(self):
        return(self.fname,self.lname,self.salary)
    def __add__(self,other):
        return (self.salary+other.salary,self.fname+other.lname)
        #return(self.fname+other.lname)
        # there is an other method which we use here example
    def __repr__(self):
       return ("Employee({},{},{})".format(self.fname,self.lname,self.salary))
    def __str__(self):
        return("The name of Employee is {}".format(self.lname))
   
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
print(h1+h2)  
print(h1.increase())
print(h2.increase())  
print(repr(h1))
print(repr(h2))
print(str(h2))
print(str(h1))
#====================================================================================================
class employee:
    def __init__(self,fname,lname,salary):
         self.fname=fname
         self.lname=lname
         self.salary=salary
         self.email=fname+lname+"@email.com"
    def increase(self):
        return(self.fname,self.lname,self.salary)
    def __add__(self,other):
        return (self.salary+other.salary,self.fname+other.lname)
        #return(self.fname+other.lname)
        # there is an other method which we use here example
    def __repr__(self):
       return ("Employee({},{},{})".format(self.fname,self.lname,self.salary))
    def __str__(self):
        return("The name of Employee is {}".format(self.lname))
   
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
print(h1+h2)  
print(h1.increase())
print(h2.increase())  
print(repr(h1))
print(repr(h2))
print(str(h2))
print(str(h1))
if (__name__=="__main__"):
    h1=employee("Mohammad","Huzaifa",440000)
    h2=employee("Mohammad","Bilal",340000)
    print(h1.email,h2.email)
#=========================================================================================================
class employee:
    def __init__(self,fname,lname,salary):
         self.fname=fname
         self.lname=lname
         self.salary=salary
         
    def increase(self):
        return(self.fname,self.lname,self.salary)
    def __add__(self,other):
        return (self.salary+other.salary,self.fname+other.lname)
        #return(self.fname+other.lname)
        # there is an other method which we use here example
    def __repr__(self):
       return ("Employee({},{},{})".format(self.fname,self.lname,self.salary))
    def __str__(self):
        return("The name of Employee is {}".format(self.lname))
    #aghr hum ya chaya ka kesii ka email change hoojaya too humay kiya kerna chaiya
    def email(self):
        return(self.fname+self.lname+"@gmail.com")
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
if(__name__=="__main__"):
    h1=employee("Mohammad","Huzaifa",440000)
    h2=employee("Mohammad","Bilal",340000)
    h2.lname="khanass"   
    print(h1.email())
    print(h2.email())
    print(h1.increase())
    print(h2.increase())
#--------------------------------------------------------------------------------------------------------------
# mujhy function koo as attribute use kerna haii too may @ property ka use kerka uskooo decarator ka toorprlooga
class employee:
    def __init__(self,fname,lname,salary):
         self.fname=fname
         self.lname=lname
         self.salary=salary
         
    def increase(self):
        return(self.fname,self.lname,self.salary)
    def __add__(self,other):
        return (self.salary+other.salary,self.fname+other.lname)
        #return(self.fname+other.lname)
        # there is an other method which we use here example
    def __repr__(self):
       return ("Employee({},{},{})".format(self.fname,self.lname,self.salary))
    def __str__(self):
        return("The name of Employee is {}".format(self.lname))
    #aghr hum ya chaya ka kesii ka email change hoojaya too humay kiya kerna chaiya
    @property
    def email(self):
        return(self.fname+"."+self.lname+"@gmail.com")
    @email.setter
    def email(self,given_email):
        name_list=given_email.split("@")[0].split(".")
        print(name_list)
        self.fname=name_list[0]
        self.lname=name_list[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
if(__name__=="__main__"):
    h1=employee("Mohammad","Huzaifa",440000)
    h2=employee("Mohammad","Bilal",340000)
    h2.lname="khanass"
    print(h1.email)#ab ya ek attribute hai ab uskoo function sign ()ki zoorat  nhhh
    print(h2.email)
    h2.email="khanan.rohan@gmail.com"
    print(h1.increase())
    print(h2.increase())
    #aghr mujhy kesi cheez ko delete kerna haiii too may use krayooga deleter
    del h2.email
    print(h2.email)
#-------------------------------------------------------------------------------------------------------
# mujhy function koo as attribute use kerna haii too may @ property ka use kerka uskooo decarator ka toorprlooga
class employee:
    def __init__(self,fname,lname,salary):
         self.fname=fname
         self.lname=lname
         self.salary=salary
         
    def increase(self):
        return(self.fname,self.lname,self.salary)
    def __add__(self,other):
        return (self.salary+other.salary,self.fname+other.lname)
        #return(self.fname+other.lname)
        # there is an other method which we use here example
    def __repr__(self):
       return ("Employee({},{},{})".format(self.fname,self.lname,self.salary))
    def __str__(self):
        return("The name of Employee is {}".format(self.lname))
    #aghr hum ya chaya ka kesii ka email change hoojaya too humay kiya kerna chaiya
    @property
    def email(self):
        if self.fname==None:
            return ("email not set")
        else:
            return(self.fname+"."+self.lname+"@gmail.com")
    @email.setter
    def email(self,given_email):
        name_list=given_email.split("@")[0].split(".")
        print(name_list)
        self.fname=name_list[0]
        self.lname=name_list[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
h1=employee("Mohammad","Huzaifa",440000)
h2=employee("Mohammad","Bilal",340000)
if(__name__=="__main__"):
    h1=employee("Mohammad","Huzaifa",440000)
    h2=employee("Mohammad","Bilal",340000)
    h2.lname="khanass"
    print(h1.email)#ab ya ek attribute hai ab uskoo function sign ()ki zoorat  nhhh
    print(h2.email)
    h2.email="khanan.rohan@gmail.com"
    print(h1.increase())
    print(h2.increase())
    #aghr mujhy kesi cheez ko delete kerna haiii too may use krayooga deleter
    del h2.email
    print(h2.email)
#------------------------------------------------------------------------------
#Question 1:
import math 
class pythagaros:
    def __init__(self,B=1,P=1):
        self.base=B
        self.Perpendicular=P
    def Formula1(self):
        global A1
        H=math.sqrt(self.base**2+self.Perpendicular**2)
        A1=0.5*self.base*H
        return("Area1 is ={}".format(A1))
    def Formula2(self):
        global A2
        H=math.sqrt(self.base**2+self.Perpendicular**2)
        A2=0.5*self.base*H
        return("Area2 is ={}".format(A2))
    def compare(self):
        global A1,A2
        if A1==A2:
            print("both area are equal")
        else:
            return("Area2 is ={}".format(A2),"Area1 is ={}".format(A1))
a1=pythagaros(2,3)
print(a1.Formula1())        
a2=pythagaros(1,2)
print(a2.Formula2())
print(a1.compare())

#-------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#Creating a vehicle management system
class vehicle_managementsystem:
    def __init__(self,N,A,P,T):
        self.Name=N
        self.Address=A
        self.postcode=P
        self.Telephone=T
    def Detail_of_tax(self,tax):
        self.taxes=tax
        return("{} your address is {} your postal address is {} and your telephone address is {} you paid a tax ={}".format(self.Name,self.Address,self.postcode,self.Telephone,self.taxes))
h1=vehicle_managementsystem("Huzaifa","5-E 9/38 ","Nazimabad karachi","03360213796")
print(h1.Detail_of_tax("34000"))   
#------------------------------------------------------------------------------------     
#LIBRARY MANAGEMENT SYSTEM:
class library:
    def location(self,Location):
        self.location=Location
class Librarian:
    def Detail(self,details,Librarian_ID):
        self.detail=details
        self.librarian=Librarian_ID
    def payment(self):
        return
    def Detail_of_library(self):
        return
    def request_of_user(self):
        return
class book_catalogy:
    def types_of_book(self,magazinebook,chemistrybook,physiscsbook,mathsbook,science_frictionbook):
        self.magazinebook=magazinebook
        self.chemistrybook=chemistrybook
        self.physics=physiscsbook
        self.mathsbook=mathsbook
        self.science_frictionbook=science_frictionbook
class book_data:
    def book_detail(self,title,subject,ISBN,shelf): 
        self.title=title
        self.subject=subject
        self.ISBN=ISBN
        self.shelf=shelf
    def Issued_date(self):
        return
    def DDS(self):
        return
class Author:
    def About_Author(self,Detail_of_Author,List_of_Author):
        self.Detail_of_Author=Detail_of_Author
        self.List_of_Author=List_of_Author
    def search(self):
        return
class User:
    def library_requirements(self,Detail,Id_approved):
        self.Detail=Detail
        self.Id_approved=Id_approved
    def request(self):
        return
    def search(self):
        return
    def complain(self):
        return
class Account:
    def Library_Account(self,login,passord):
        self.login=login
        self.passord=passord




#-----------------------------------------------------------------------------------------------
#lab 2 manual question:
#Question 1:        

class Person:
# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Instantiate the Person object
person1= Person("ali", 6)
print(person1.name,person1.age)
person2 = Person("ahmed", 9)
print(person2.name,person2.age) 
#--------------------------------------------------------------------------   
#question 2:
class Person:
    def __init__(self,name,weight,age):
        self.name=name
        self.weight=weight
        self.age=age
    def description(self):
        return(self.name,self.weight,self.age)
        
person1=Person("Huzaifa","None",20)
print(person1.description())
person2=Person("Bilal","None",25)
print(person2.description())
person3=Person("Maha","None",16)
print(person3.description())        
#------------------------------------------------------------------------------------------------------------------

#Question 3:
#child class ko derived class or sub class bhi kha jata haiiiii child ka pass excess hota haiiiii
# parent classs koo super class bhi kha jata haiiii

# parent class
#------------------------------# using concept of single inheritance::-------------------------------------------
class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age
    def printdetails(self):
        print(self.name, self.age)
# child class
class Employee(Person):
    def __init__(self, name, age, post):
# invoking the __init__ of the parent class
        Person.__init__(self, name, age)
        self.post = post
    def Details(self):
        print("Employee Data Name age and post is ",self.name, self.age, self.post)
#creation of an object or an instance
E1 = Employee("ali", 35,"Clerk")
E1.Details()
E1.printdetails()
#------------------------------------------
E2=Employee("huzii",20,"None")
E2.Details()


#-------------------------------------------------------------------------------------------------------------------
#Question 2 lab 3 oops
class residential_house:
    def __init__(self,type_of_house,location_of_the_house,room_in_house,story,parking,prize_of_the_house):
        self.type_of_house=type_of_house
        self.location_of_the_house=location_of_the_house
        self.room_in_house=room_in_house
        self.story=story
        self.parking=parking
        self.prize_of_the_house=prize_of_the_house
    def  Big_house(self):
        return ("The type of house is {}"
                "\n the location of house is {}"
                "\n rooms in the house is {}\n story of the house is{}\n parking avability of the house is {}"
                "\n prize of the house is {}".
                format(self.type_of_house,self.location_of_the_house,self.room_in_house, self.story,self.parking,self.prize_of_the_house))
        
class Commercial_house(residential_house):
    def __init__(self,type_of_house,location_of_the_house,room_in_house,story,parking,prize_of_the_house):
        super().__init__(type_of_house,location_of_the_house,room_in_house,story,parking,prize_of_the_house)
    def small_house(self):
           return ("The type of house is {}"
                "\n the location of house is {}"
                "\n rooms in the house is {}\n story of the house is{}\n parking avability of the house is {}"
                "\n prize of the house is {}".
                format(self.type_of_house,self.location_of_the_house,self.room_in_house, self.story,self.parking,self.prize_of_the_house))
             
C_h=Commercial_house("Appartment","123-5-E 9/38 rst road Karachi",4,"this appartment has 10 story","Their is no parking avability","54 lac")
print(C_h.small_house())

R_h=residential_house("Bungaloo","DHA phase 5 ",5,"the bungaloo have only single story","parking avability in the bungaloo","mosthly 5 core")
print(R_h.Big_house())

#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------- using multilevel inheritance---------------------------------------------------
#-------------------------------- by sir faisal program------------------------------------------------------------------
#when a child class become a parent class of other child class
class Mainparent:
    def func1(self):
        return("I am from main parent class")
        
class Firstclass(Mainparent):
    def func2(self):
        return("I am from First child")
class secondclass(Firstclass):
    def func3(self):
        return("I am from second child")
obj=Firstclass()
print(obj.func2())
obj1=secondclass()
print(obj1.func3())
print(obj1.func1())
print(obj1.func2())  
obj=Mainparent()
print(obj.func1())      
        
#-----------------------------------------------------------------------------------------------------------------------------
class Employee:
    def func1(self):
        return("I am from Employee Class")
class Faculty(Employee):
    def func2(self):
        return("I am from Faculty and sub class of employee")
class JuniorFaculty(Faculty):
    def func3(self):
        return("I am from JuniorFaculty and subclass of faculty")
obj_jnFa=JuniorFaculty()
print(obj_jnFa.func2())

obj_jnFa=JuniorFaculty()
print(obj_jnFa.func1())
print(obj_jnFa.func2())
print(obj_jnFa.func3())       

obj_jnFa=Employee()
print(obj_jnFa.func1())
#------------------------------------------------------------------------------------------------------------------------------
class Level1:
    def game1(self):
        return("Hello and Welcome to street fighter of game level round 1")
    def fighter1(self):
        self.fighter=10
        return(self.fighter)
    def enemy1(self):
        self.enem=5
        return(self.enem)
class level2(Level1):
    def game2(self):
        return("Hello and Welcome to street fighter of game level round 2")
    def fighter2(self):
        self.fighter=20
        return(self.fighter)
    def enemy2(self):
        self.enemy1=5
        self.enemy2=20
        return(self.enemy1,self.enemy2)
class Level3(level2):
    def game3(self):
        return("Hello and Welcome to street fighter of game level round 3")
    def fighter3(self):
        self.fighter=100
        return(self.fighter)
    def boss3(self):
        self.boss=85
        return(self.boss)
l1=Level3()
print(l1.game3())
print(l1.fighter3())
print(l1.boss3())
print(l1.game2())
print(l1.fighter2())
print(l1.enemy2())
print(l1.game1())
print(l1.fighter1())
#---------------------------------------------------------------------------------------------------------------------       
class Family:
    def show_family(self):
        return("This is our family:")
        
# Father class is inherited from fami
class Father(Family):
    fathe_name=""
    def show_father(self):
        print(self.fathe_name)
#mother class also inherited from family
class Mother(Family):
    mother_name=""
    def show_mother(self):
        print(self.mother_name)
# son classes also inherited from father and mother classes:
class son(Father,Mother):
    myname="Huzaifa"
    def show_parents(self):
        print("Father is",self.fathe_name)
        print("Mother is ",self.mother_name)
    def introo(self):
        print("I am a son of",self.fathe_name , "and my mother name is",self.mother_name , "and you call me" ,self.myname)
s1=son()
s1.fathe_name="Sohail"
s1.mother_name="Nazia"
s1.show_family()
s1.show_father()
s1.show_mother()
s1.show_parents()
s1.introo()        
#-----------------------------------------------------------------------------------------------------------------------
# here we use multiple inheritance concept in which there are two different classes
# and both different class is inherited to its subclass 
class employee:
    var1=8
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        print(self.salary)
        print(self.fname)
        print(self.lname)
class player:
    var2=9
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print_details(self):
        return("The man is",self.name ,"and the game is",self.game)
class coolprogrammer(employee,player):#yahan pr programmer ek dusarii class haii joo inherit haii upper walii class say likin 
    #eska oject ki help say may nay upper wali class ka attributes koo call kiyaaa
    var3=10
    language="Python"
    def printlanguage(self):
        print(self.language)                            #multiple inheritance may es cheez ka khail rakhan zoorarii haii
huzaifa1=employee("Muhammad","Huzaifa",45000)           # kaa hamesha order of classes same rahaygiiiii verna sb ulta sadiya                                                                                 
huzaifa=employee("Muhammad","Bilal",23000)                  # hoojaya gaaaaa
print(huzaifa1.increase())
print(huzaifa1.increase())    
bilal=player("bilal",["football"])    
print(bilal.print_details())
kamran=coolprogrammer("muhammad","Omar",45000)
print(kamran.printlanguage()) 
print(kamran.var1) 
print(kamran.var2)
print(kamran.var3)  
#--------------------------------------------------------------------------------------------------------------    
    def __init__(self,aboutprogrammer):
        self.aboutprogrammer=aboutprogrammer
        super().__init__(fname,lname,salary)
        super().__init__(lname,game)
    def print_infoo(self):
        return("The first name of employee is {} and the last name of 
               "employee is {} and the salary of {} is {} ")
#-------------------------------------------------------------------------------------------------------------
#using concept of Multilevel in heritance::::
class dad:
    #basketball=9
    pass
class son(dad):
    pass
    basketball=124
    dance=1
    def isdance(self):
        return f"Yes i am dance{self.dance} no of times"
class grandson(son):
    dance=6
    def isdance(self):
        return f"jackson yeah!"\
               f"Yes i am dance {self.dance} no of times"    
darry=dad()
larry=son()
harry=grandson()
print(harry.isdance()) 
print(harry.dance)              
print(harry.basketball)
#----------------------------------------------------------------------------------------------------------------
class ElectronicDevice:
    inheritance_level=0
    def electronic(self):
        print(f"You are in Electronics Shop and enheritance level "
              f"is {self.inheritance_level}")
    pass
class PocketGadget(ElectronicDevice):
    inheritance_level=1
    def pocket(self):
        print(f"You are in Gadget shop and enheritance level "
              f"is {self.inheritance_level}")
    pass
class Phone(PocketGadget):
    inheritance_level=2
    def phone(self):
        print(f"You are in phone class and enheritance level "
              f"is {self.inheritance_level}")
    pass
electronic = ElectronicDevice()
electronic.electronic()
gadget=PocketGadget()
gadget.pocket()
phone=Phone()
phone.phone()
#----------------------------------------------------------------------------------------------------------------
class electronic_device:
    laptop = "ASUS"
    core = "AMD RYZEN 5"
    price1 = 32000
    def islaptop(self):
        return f" This is {self.laptop} Laptop with {self.core} processor in just Rs. {self.price1} "
class pocket_gadgets(electronic_device):
    name1 = "BoAt"
    size = 3.5
    price2 = 399
    def isearphone(self):
        return f"After Buying {self.laptop} Laptop You will Get these Earphones Having {self.size} mm Jack AND with in Just {self.price2}"
class phone(pocket_gadgets):
    name2 = " Redmi Y1"
    ram = "3/32"
    battery = 3050
    price3 = 8000
    def isphone(self):
        return f" If you dont want that {self.laptop} laptop and {self.name1} Earphones deal then just Buy this {self.name2} Phone with {self.ram} variant in just {self.price3} Rupees"
device = electronic_device()
gadget = pocket_gadgets()
smartphone = phone()
print(smartphone.isphone())
#------------------------------------------------------------------------------------------------------------------
class Electronic_device():
    power_source = "Alternating current or Direct Current"
    use = "Automates works and make the work very faster and efficient"
    start = "It is a kind of device which uses"
   
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}".capitalize()

class Pocket_gadget(Electronic_device):
    power_source = "Direct current"
    addon_features = "It is portable and looks super awesome"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()

class Phone(Pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


computer = Electronic_device()
miband = Pocket_gadget()
redmi = Phone()

print(computer.printdetails())
print(miband.printdetails())
print(redmi.printdetails())
#-----------------------------------------------------------------------------------------------------------
#concept of public,protected,private
#hum jitnay bhii variable python may use kertay hai woo saray public hotay haiii
#han aghr mujhy kesi cheez koo protexted kerna haii to may uskooo esthara likooga (_protected)
#han aghr mujhy kesi cheez koo private kerna hai jesko may excess kerpayooo too woo esthara likha jaya gaaa (__private)
#Example
class data:
    _protected=9 # this variable is now protected yanii essay saray meray ghr walay dhek saktay haiii
    public=12344675#this variable is public eskoo sb excess kersaktay haiiii
    __private=36613873#this variable is private jesay may excess kersakta hoo khaliiiiii
    def __init__(self,distance,time):
        self.distance=distance
        self.time=time
    def formula(self):
        v=self.distance//self.time
        return("velocity={}m/s".format(v))
f1=data(100,4)
print(f1.formula())        
print(f1._protected)
print(f1._data__private)# to written in this form(_data__private) is called "namemangling" python nay aesa esliya kiya ku ka esnay us variable koo private kerdiya jabhii joo sirf uski class say hiii excess hosakta haiii
print(f1.public)
#---------------------------------------------------------------------------------------------------------------
#----------------------------------------- polymerhiom in pyhton------------------------------------------------
#polymorhism is basiciallyy a concept "abality of doing in diffreent form"
print(6+3)# these are both number are integers 
print("5"+"6")#these number are string and they are combing with each other
#--------------------------------------------------------------------------------------------------------------
class Animals: 
      
    # Initializing constructor 
    def __init__(self): 
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
      
    def isMammal(self): 
        if self.isMammal: 
            print("It is a mammal.") 
      
    def isDomestic(self): 
        if self.mammals: 
            print("It is a domestic animal.") 
      
class Dogs(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def isMammal(self): 
        super().isMammal() 
  
class Horses(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def hasTailandLegs(self): 
        if self.tail and self.legs == 4: 
            print("Has legs and tail") 
  
 
obj_dog = Dogs() 
obj_dog.isMammal() 
obj_hourse = Horses() 
obj_hourse.hasTailandLegs() 
#--------------------------------------------------------------------------------------------------------------
# Python program to demonstrate 
# hybrid inheritance 
class School: 
     def func1(self): 
         print("This function is in school.") 
   
class Student1(School): 
     def func2(self): 
         print("This function is in student 1. ") 
   
class Student2(School): 
     def func3(self): 
         print("This function is in student 2.") 
   
class Student3(Student1,Student2): 
     def func4(self): 
         print("This function is in student 3.") 
class Student4(Student2,School):
    def func5(self):
        print("This function is in student 4")         
   
 
object = Student3() 
object.func1() 
object.func2()            
object.func4()
object=Student4()   
object.func5()
object.func3()
object.func1()
#--------------------------------------------------------------------------------------------------------------
#Example 1:
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        self.classvar1="I am in class A"#instance object haii yaa
class B(A):
    classvar2="I am in class B" 
a=A()
b=B() 
print(b.classvar1) # python program koo run esthara krayga sbsay phalay woo class B may jayaga or check krayga ka koi
#instance variable too nh haiii classs B may aghr nh hai too woo phir jayagaaa ka class bB kesay inherit hoi haii 
#or jesay say woo inherit hoi haiii haii aghr instance variable usmay hai to wooo uskoo print kerdyga aghr usmay bhi
# nh hoya too wooo kuch nh print keraygaa
#----------------------------------------------------------------------------------------------------------
#Example 2
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        #self.classvar1="I am in class A"#instance object haii yaa
class B(A):
    classvar2="I am in class B" 
a=A()
b=B() 
print(b.classvar1)# usnay class A ka variable koo print kerdiya ku kaaa maynay method classvar1 usekiya thaa
#------------------------------------------------------------------------------------------------------------
#Example 3:
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        #self.classvar1="I am in class A"#instance object haii yaa
class B(A):
    classvar1="I am in class B" #aghr may yahan bhiii var1 kerdoo too kiya hooga 
a=A()
b=B() 
print(b.classvar1)#too phir woo sb say phalay class b ka variable print kerdygaaa 
#-------------------------------------------------------------------------------------------------------------
#Example 4:
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        #self.classvar1="I am in class A"#instance object haii yaa
class B(A):
    pass
    #classvar1="I am in class B" #aghr may yahan bhiii var1 kerdoo too kiya hooga 
a=A()
b=B() 
print(b.classvar1)# ab usnay class A ka variable koo print kerdiya 
#-------------------------------------------------------------------------------------------------------------
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        self.classvar1="I am in class A"#instance object haii yaa
class B(A):
    classvar1="I am in class B" #aghr may yahan bhiii var1 kerdoo too kiya hooga 
    def __init__(self):
        self.var1="i am inside a constructor of class B"
        self.classvar1="I am in class B"
a=A()
b=B() 
print(b.var1,b.classvar1)
#------------but aghr mayy eskooo inherit kerdoo class A ka constructor say kiya hooga -------------------------
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        self.classvar1="I am in class A"#instance object haii yaa
        self.special="special"
class B(A):
    classvar1="I am in class B" #aghr may yahan bhiii var1 kerdoo too kiya hooga 
    def __init__(self):
        super().__init__()#yahan usnay Class A ka constructor koo call ki likin classvar1or var1 ki value classB ka constructor may change hoogi too usnay classB ka constructor ki value diii
        self.var1="i am inside a constructor of class B"
        self.classvar1="I am in class B"
a=A()
b=B() 
print(b.special,b.classvar1)
#---------------------------------------------------------------------------------------------------------------
class A:
    classvar1="I am a variable in class 1 A"# class object haii yaaa
    
    def __init__(self):
        self.var1="i am inside a constructor of class A"
        self.classvar1="I am in class A"#instance object haii yaa
        self.special="special"
class B(A):
    classvar1="I am in class B" #aghr may yahan bhiii var1 kerdoo too kiya hooga 
    def __init__(self):
        #super().__init__()
        self.var1="i am inside a constructor of class B"
        self.classvar1="I am in class B"
        super().__init__()#yahan usnay Class B ka constructor koo call ki likin classvar1or var1 ki value classA ka constructor may change hoogi too usnay classA ka constructor ki value diii
        print(super().classvar1)
a=A()
b=B() 
print(b.special,b.classvar1,b.var1)
#-----------------------------------------------------------------------------------------------------------------
# using a objectintrospection 
# object introspection ka matlab kiya hoota haiii eska matlab ya hoota haiii ka object ki type kiya 
# haii object kes class say belong kerta haiii uskii information laynaaa
#Example 1:
class data:
    def __init__(self,distance,time):
        self.distance=distance
        self.time=time
    def formula(self):
        v=self.distance//self.time
        return("velocity={}m/s".format(v))
f1=data(100,4)
print(f1.formula())
print(type(f1))        
print(type("this string belong to a string class"))
#easii thara her object kii diiferent id hoti haiiii 
print(id("each a every object has a unique id "))
print(id("I tell you each and every object has a unique id"))
#ab hum ek or objectintrospection ka use kertay haiii
ab="I am using dir method to find object introspection"
print(dir(ab))
#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------
class MainParent:
      def func1(self):
          print("I am from Main Parent Class")
class FirstChild(MainParent):
      def func2(self):
          print("I am from First Child")

class SecondChild(FirstChild):
    def func3(self):
        print("I am from Second Child")

obj = FirstChild()
obj.func2()

obj2 = MainParent()
obj2.func1()

obj1 = SecondChild()
obj1.func3()
obj1.func2()
obj1.func1()
#-------------------------------------------------------------------------------------------
class Employee:
      def func1(self):
          print("I am from Employee Class")
class Faculty(Employee):
      def func2(self):
          print("I am from Faculty and sub class of Employee")

class JuniorFaculty(Faculty):
    def func3(self):
        print("I am from Junior Faculty and sub class of Faculty")

fac_obj = JuniorFaculty()
fac_obj.func2()

jun_facobj = Employee()
jun_facobj.func1()

jfobj1 = JuniorFaculty()
jfobj1.func3()
jfobj1.func2()
jfobj1.func1()
#---------------------------------------------------------------------------------------
class Family:
    def show_family(self):
        print("This is our family:")
 
 
# Father class inherited from Family
class Father(Family):
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class inherited from Family
class Mother(Family):
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    myname ='Ahmed'
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
    
    def my_intro(self):
        print("I am son of ", self.fathername + " and my mother name is", self.mothername + " you can call me ", self.myname)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Turab"
s1.mothername = "Amna"
s1.show_family()
s1.show_parent()
s1.my_intro()
#-----------------------------------------------------------------------------------------
class Animals: 
      
    # Initializing constructor 
    def __init__(self): 
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
      
    def isMammal(self): 
        if self.isMammal: 
            print("It is a mammal.") 
      
    def isDomestic(self): 
        if self.mammals: 
            print("It is a domestic animal.") 
      
class Dogs(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def isMammal(self): 
        super().isMammal() 
  
class Horses(Animals): 
    def __init__(self): 
        super().__init__() 
  
    def hasTailandLegs(self): 
        if self.tail and self.legs == 4: 
            print("Has legs and tail") 
  
 
obj_dog = Dogs() 
obj_dog.isMammal() 
obj_hourse = Horses() 
obj_hourse.hasTailandLegs()
#-----------------------------------------------------------------------------------------
# Python program to demonstrate 
# hybrid inheritance 
  
  
class School: 
     def func1(self): 
         print("This function is in school.") 
   
class Student1(School): 
     def func2(self): 
         print("This function is in student 1. ") 
   
class Student2(School): 
     def func3(self): 
         print("This function is in student 2.") 
   
class Student3(Student1, School): 
     def func4(self): 
         print("This function is in student 3.") 
   
 
object = Student3() 
object.func1() 
object.func2() 
#-------------------------------------------------------------------------------------------
#single inheritance concept
#Task1
class  Vehicle:
    
    def __init__(self,name,model_no,color,price,registration_year):
        self.name=name
        self.model_number=model_no
        self.color=color
        self.price=price
        self.registration_year=registration_year
    
    def toyota_vehicle(self):
        return f" name of car is: {self.name} \n model of car is: {self.model_number} \n color of car is: {self.color} \n price of car is: {self.price}\n year of registration of car is: {self.registration_year} \n "
        
    

class  luxury_car(Vehicle):
    
    def luxury_toyota_vehicle(self):
        return f" name of car is: {self.name} \n model of car is: {self.model_number} \ncolor of car is: {self.color} \n price of car is: {self.price} \n year of registration of car is: {self.registration_year} \n "


    
cars=Vehicle("Corolla","ABC-1234","white",2000000,2019)  
luxury_cars=luxury_car("Fortuner","DEF-5678","silver",4000000,2019)  

print(cars.toyota_vehicle())
print(luxury_cars.luxury_toyota_vehicle())

#------------------------------------------------------------------------------------------
#Task 2
#Create a class of Tree with Child (any type of tree) and print them.
class Tree:
    def __init__(self,soil,fruits,leaves):
        self.soil=soil
        self.fruits=fruits
        self.leaves=leaves
class MangoTree(Tree):
    def __init__(self,soil,fruits,leaves):
        super().__init__(soil,fruits,leaves)
    def  Age(self):
        return("The Soil used in the tree is {} and It is a tree of {} and It has a {} ".format(self.soil,self.fruits,self.fruits))
F=MangoTree("[Ammoniumnitrate,Ammoniumsulphide ]","Mangoes","shadyleaves")    
print(F. Age()) 
#-----------------------------------------------------------------------------------------
#Task3
#Create a class of Book with Child (any topic and title of book) and print them.
class Book:
    def __init__(self,title,author,translator,published,ISBN):
        self.title=title
        self.author=author
        self.translator=translator
        self.published=published
        self.ISBN=ISBN
        
    def About_book(self,Main_characters):
        self.Main_characters=Main_characters
        return(f"The original title of the book is {self.title}\n"\
               f"The author of the book is{self.author}\n" \
               f"The translator of this book is{self.translator}\n"\
               f"This book was published in {self.published}\n"\
               f"The ISBN number is {self.ISBN}\n"
               f"The main characters of the story are {self.Main_characters}\n")
class pages(Book):
    def numbers(self,pages):
        self.pages=pages
        return("This book contain {} pages \n".format(self.pages))
obj=pages("Le Comte de Monte-Cristo"," Alexandre Dumas"," Robin Buss","Published May 27th 2003 by Penguin Classics (first published 1844)"," (ISBN13: 9780140449266)")
print(obj.About_book("[CharactersEdmond Dantès,\n Abbé Faria,\n Giovanni Bertuccio,\n Luigi Vampa,\n Haydée,\n Mercédès Mondego,\n Fernand Mondego,\n Albert de Morcerf,\n Baron Danglars, \n,Gérard de Villefort,\n Valentine de Villefort,\n Noirtier de Villefort,\n Héloïse de Villefort,\n Pierre Morrel,\n Maximilien Morrel,\n Beauchamp,\n Franz d'Épinay,\n Lucien Debray,\n Eugénie Danglars,\n Hermine Danglars,\n Benedetto, Kadrus ]"))
print(obj.numbers(1276))
#-------------------------------------------------------------------------------------------
#Create a class of airplane with Children (any two different types of planes such as fighter and passenger) and print them.
class Airplane:
    def __init__(a,speed,weight,color):
        a.speed=speed
        a.weight=weight
        a.color=color
class passengerplane(Airplane):
    def __init__(a,speed,weight,color):
        super().__init__(speed,weight,color)
    def takeOff(a):
        return("This is PassangerPlane It fly with speed of {} It weight is {} and has a color of {}".format(a.speed,a.weight,a.color))
class fighterplane(Airplane):
    def __init__(a,speed,weight,color):
        super().__init__(speed,weight,color)
    def takeOff(a):
        return("This is JF-17PThunder It fly with speed of {} It weight is {} and has a color of {}".format(a.speed,a.weight,a.color))
P=passengerplane("926km/h","175,000 lbs","white")
print(P.takeOff())
F=fighterplane("1.8Mach","6,586kg","Grey")
print(F.takeOff())
#--------------------------------------------------------------------------------------------
#Create a class of plant with Children (any type of plants such as roses and decoration) and print them.
class Plant:
    def __init__(self,rootsystem, stamen, leaves,shootSystem):
        self.rootsystem=rootsystem
        self.stamen=stamen
        self.leaves=leaves
        self.shootSystem=shootSystem
class Rose_Plant(Plant):
    def __init__(self,rootsystem, stamen, leaves,shootSystem):
        super().__init__(rootsystem, stamen, leaves,shootSystem)
    def SweetSmell(self):
        return("The rootsystem has {} Stamen include {} and growing of leaves process include {} and shootsystem has{}".format(self.rootsystem, self.stamen, self.leaves,self.shootSystem))
P=Rose_Plant("Respirationprocess","PollinateProcess","[Do Photosynthesis,Do Respirstion]","[Do diameter Growth,Do Respirstion ,Making_of_leaves,Make Stamen,Do photosynthesis]")      
print(P.SweetSmell())  
#-------------------------------------------------------------------------------------------
class residential_houses:
    
    def __init__(self,type_of_house,location_of_house,rooms_in_the_house,story,parking):
        self.type_of_house=type_of_house
        self.location_of_house=location_of_house
        self.rooms_in_the_house=rooms_in_the_house
        self.story=story
        self.parking=parking
    
    def big_house(self):
        return f" the type of house is: {self.type_of_house} 
    \n location of the house is: {self.location_of_house} 
        \n rooms in the house is: {self.rooms_in_the_house} \n location of the house is: {self.story}
                \n parking is available or not: {self.parking} \n "

class  commercial_houses(residential_houses):
    
    def small_house(self):
        return f" the type of house is: {self.type_of_house} \n location of the house is: {self.location_of_house}
        \n rooms in the house is: {self.rooms_in_the_house} \n location of the house is: {self.story}
        \n parking is available or not: {self.parking} \n "

    
residential_house=residential_houses("Bungalo","123-ABC xyz road Karachi",20,"the bungalo have only one story",
                                     "parking is available in the bungalo")  
commercial_house=commercial_houses("appartment","456-LMN rst road Karachi",4,"this appartment have 10 floors",
                                   "Parking is not available in the appartment")  
  

print(residential_house.big_house())
print(commercial_house.small_house())
#-------------------------------------------------------------------------------------------
class Parent():
       def intro(self):
           print('I am a Parent')
 
class Child(Parent):
       def myintro(self):
          print('I am a Child')
 
ob1 = Child()
ob1.intro()
ob1.myintro()
#-----------------------------------------------------------------------------------------
class Parent:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     
     def view(self):
         print(self.firstname , self.age)

            
class Child(Parent):
     def __init__(self , fname , fage):
          Parent.__init__(self, fname, fage)
          self.lastname = "Ali"
     
     def view(self):
          print("My name is " , self.firstname ,". I am  ",  self.age , " years old." ,  " My friends usually call me by family name which is ",self.lastname)

child_ob = Child("Syed Faisal" , '45')
child_ob.view()
#---------------------------------------------------------------------------------------------
class Parent1:
   def intro1(self):
        print("I am from Parent 1 Class")
class Parent2:
   def intro2(self):
        print("I am from Parent 2 Class")

class Child(Parent1 , Parent2):
    def intro3(self):
        print("I am from Child Class")
 
child_ob = Child()
child_ob.intro1()
child_ob.intro2()
child_ob.intro3()
#----------------------------------------------------------------------------------------------
class employee:
    pass
#huzaifa is an object of employeee
huzaifa=employee()
#similarly bilal is an object of employee
bilal=employee()
#here we assigning a instance variable
huzaifa.name="huzi"
bilal.name="billliii"
print(huzaifa.name,",",bilal.name)
#---------------------------------------------------------------------------------------------
class employee:
    noofleaves=8
    def printdetails(self):
        return f"th name of{self.name},roll number is{self.roll},and the section is{self.section}"
        
    
     
huzaifa=employee()
bilal=employee()
huzaifa.name="huzaifa"
huzaifa.roll="165"
huzaifa.section="b"
employee.noofleaves=9
print(huzaifa.printdetails())
print(huzaifa.noofleaves)

#---------------------------------------------------------------------------------------------
class employee:
    def __init__(self,aname,asection,arollnumber):
        self.name=aname
        self.section=asection
        self.roll=arollnumber
    
    
    def printdetails(self):
        return f"th name of{self.name},roll number is{self.section},and the section is{self.roll}"
        
    
     
huzaifa=employee("huzaifa","b","139")
#bilal=employee()
#huzaifa.name="huzaifa"
#huzaifa.roll="165"
#huzaifa.section="b"
print(huzaifa.section)
print(huzaifa.printdetails())
#-------------------------------------------------------------------------------------------
class employee:
    #assigning variable in class
         noleaves=8
         pass
    # this vaiable is the class and huzaifa and bilal is sharing this variable 
    
    
#huzaifa=employee()
bilal=employee()
#huzaifa.name="huzi"
#huzaifa.rollnumber=139
#huzaifa.student ="UIT"
bilal.student ="little.folk"
bilal.rollnumber=23
bilal.name="billliii"
print(bilal.name,",",bilal.student,",",bilal.rollnumber,",",huzaifa.name,",",huzaifa.student,",",huzaifa.rollnumber)
#---------------------------------------------------------------------------------------------
#decroater
def function1():
    print("subcribe now")
func_2=function1
func_2()
#--------------------------------------------------------------------------------------------
#dectrotars
def funcrets(nums):
    if nums==0:
        return print
    if nums==1:
        return sum
#a=funcrets(0)
a=funcrets(1)
        

print(a)
#--------------------------------------------------------------------------------------------
#Task 2
#Create a class of Tree with Child (any type of tree) and print them.
class Tree:
    def __init__(self,soil,fruits,leaves):
        self.soil=soil
        self.fruits=fruits
        self.leaves=leaves
class MangoTree(Tree):
    def __init__(self,soil,fruits,leaves):
        super().__init__(soil,fruits,leaves)
    def  Age(self):
        return("The Soil used in the tree is {} and It is a tree of {} and It has a {} ".format(self.soil,self.fruits,self.fruits))
F=MangoTree("[Ammoniumnitrate,Ammoniumsulphide ]","Mangoes","shadyleaves")    
print(F. Age()) 
#-----------------------------------------------------------------------------------------------
#Task3
#Create a class of Book with Child (any topic and title of book) and print them.
class Book:
    def __init__(self,title,author,translator,published,ISBN):
        self.title=title
        self.author=author
        self.translator=translator
        self.published=published
        self.ISBN=ISBN
        
    def About_book(self,Main_characters):
        self.Main_characters=Main_characters
        return(f"The original title of the book is {self.title}\n"\
               f"The author of the book is{self.author}\n" \
               f"The translator of this book is{self.translator}\n"\
               f"This book was published in {self.published}\n"\
               f"The ISBN number is {self.ISBN}\n"
               f"The main characters of the story are {self.Main_characters}\n")
class pages(Book):
    def numbers(self,pages):
        self.pages=pages
        return("This book contain {} pages \n".format(self.pages))
obj=pages("Le Comte de Monte-Cristo"," Alexandre Dumas"," Robin Buss","Published May 27th 2003 by Penguin Classics (first published 1844)"," (ISBN13: 9780140449266)")
print(obj.About_book("[CharactersEdmond Dantès,\n Abbé Faria,\n Giovanni Bertuccio,\n Luigi Vampa,\n Haydée,\n Mercédès Mondego,\n Fernand Mondego,\n Albert de Morcerf,\n Baron Danglars, \n,Gérard de Villefort,\n Valentine de Villefort,\n Noirtier de Villefort,\n Héloïse de Villefort,\n Pierre Morrel,\n Maximilien Morrel,\n Beauchamp,\n Franz d'Épinay,\n Lucien Debray,\n Eugénie Danglars,\n Hermine Danglars,\n Benedetto, Kadrus ]"))
print(obj.numbers(1276))
#---------------------------------------------------------------------------------------
#Create a class of airplane with Children (any two different types of planes such as fighter and passenger) and print them.
class Airplane:
    def __init__(a,speed,weight,color):
        a.speed=speed
        a.weight=weight
        a.color=color
class passengerplane(Airplane):
    def __init__(a,speed,weight,color):
        super().__init__(speed,weight,color)
    def takeOff(a):
        return("This is PassangerPlane It fly with speed of {} It weight is {} and has a color of {}".format(a.speed,a.weight,a.color))
class fighterplane(Airplane):
    def __init__(a,speed,weight,color):
        super().__init__(speed,weight,color)
    def takeOff(a):
        return("This is JF-17PThunder It fly with speed of {} It weight is {} and has a color of {}".format(a.speed,a.weight,a.color))
P=passengerplane("926km/h","175,000 lbs","white")
print(P.takeOff())
F=fighterplane("1.8Mach","6,586kg","Grey")
print(F.takeOff())
#------------------------------------------------------------------------------------------------
# Multiple Inheritance
#Create a class of plant with Children (any type of plants such as roses and decoration) and print them.
class Plant:
    def __init__(self,rootsystem, stamen, leaves,shootSystem):
        self.rootsystem=rootsystem
        self.stamen=stamen
        self.leaves=leaves
        self.shootSystem=shootSystem
class Rose_Plant(Plant):
    def __init__(self,rootsystem, stamen, leaves,shootSystem):
        super().__init__(rootsystem, stamen, leaves,shootSystem)
    def SweetSmell(self):
        return("The rootsystem has {} Stamen include {} and growing of leaves process include {} and shootsystem has{}".format(self.rootsystem, self.stamen, self.leaves,self.shootSystem))
P=Rose_Plant("Respirationprocess","PollinateProcess","[Do Photosynthesis,Do Respirstion]","[Do diameter Growth,Do Respirstion ,Making_of_leaves,Make Stamen,Do photosynthesis]")      
print(P.SweetSmell())  
#------------------------------------------------------------------------------------------------------------
#Task (a) 
#Create a class for representing family with Parents from two seperate classes 
#(make one Parent class from Father, other from Mother and create their child) and print them.
class Family:
    def intro(self):
        return("this is our Family")
class Father(Family):
    Father=""
    def Intro1(self):
        return("My Father Name is {}".format(self.Father))
class Mother(Family):
    Mother=""
    def Intro2(self):
        return("My Mother Name is {}".format(self.Mother))
class Son(Father,Mother):
    Name=""
    def Intro3(self):
        return("I am a son of {} and my name is {}".format(self.Father,self.Name))        
s=Son() 
s.Father="Sohail Siddique"
s.Mother="Naziz Siddique"
s.Name="Huzaifa Siddique"
print(s.intro())
print(s.Intro1())
print(s.Intro2())
print(s.Intro3())  
#-------------------------------------------------------------------------------------------------
#Task (b) 
#Create a class for computer fighter game in which we have Class Computer_Player
#using two or three seperate Classes (boxer class, judo class, kickboxing class then create a child) 
#and print them.
class FighterGame:
    print("welcome to Game Prince of Persia")
class Round1:
    print("Round 1 Save the city from judhooo and get its sord")
class primaryweapon:
    def __init__(self,sord,Axe,Armour):
        self.sord=sord
        self.Axe=Axe
        self.Armour=Armour
    def wm(self):
        return("The fighter has {} and {} and {} to protect it self".format(self.sord,self.Axe,self.Armour))
class Enemy1:
    def caputured(self,name,sord1):
        self.name=name
        self.sord1=sord1
        return ("my name is {} and I want to captured the city And become am the king and this {} is My ".format(self.name,self.sord1))
    
class Prince(primaryweapon,Enemy1):
    def defender(self,name1):
        self.name=name1
        return ("I am {} the prince of this city I save my city and get your {}".format(self.name,self.sord1))
a=FighterGame()
a=Round1()
P=Prince("[Eaglesord,serpentsord,spidersord,Dagger]","[Ages,Airyaman]","[shieldArmour,Ahura]")
print(P.caputured("Judhoo","watersord"))
print(P.defender("Umachii"))
print(a)

#------------------------------------------------------------------------------------------------
#Task (c) 
#Create a class representing RGB color using three different Class Red, 
#Green and Blue(create some objects which have differnt RGB values) and print them.
class RGB:
    print("we seen any image on screen due to this rgb color ")
class Red:
    red_hexa_value=""
    red_decimal_value=""
    def value1(self):
        return("we can make red color by taking value in this form {} or in this form {}".format(self.red_hexa_value,self.red_decimal_value)) 
class Green:
    green_hexa_value=""
    green_decimal_value=""   
    def value2(self):
         return("we can make green color by taking value in this form {} or in this form {}".format(self.green_hexa_value,self.green_decimal_value))    
class Yellow:
    yellow_hexa_value=""
    yellow_decimal_value=""
    def value3(self):
         return("we can make yellow color by taking value in this form {} or in this form {}".format(self.yellow_hexa_value,self.yellow_decimal_value))    
class Color(Red,Green,Yellow):
    print("we can use both method to give color value")
A=RGB()
print(A)    
C=Color()
C.red_hexa_value="#FF0000"    
C.red_decimal_value="rgb(255,0,0)"
C.green_hexa_value="#008000"
C.green_decimal_value="rgb(0,128,0)"
C.yellow_hexa_value="#FFFF00"
C.yellow_decimal_value="rgb(255,255,0)"    
print(C.value1())
print(C.value2())
print(C.value3())        
#-----------------------------------------------------------------------------------------------
# task 1
#Creat a class of Point. Use two variables for x axis and y axis. 
#Create two objects p1 and p2. find the difference between the points of p1.x with p2.x and 
#similarly p1.y with p2.y. You can use method just like reset(). Make method difference().
import math
class point:
    def reset(self):
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
    def difference(self):
       d=math.sqrt((self.x2-self.x1)**2)+((self.y2-self.y1)**2)
       print("The Distance between two point is {}".format(d))   
p=point()    
p.x1=3
p.y1=4
p.x2=5
p.y2=6
p.difference()
print(p.x1,p.x2)
p.reset()
print(p.x1,p.y1)
print()
#------------------------------------------------------------------------------------------------
import math
class vector:
    def Vector1_points(self,x1=0,y1=0,x2=0,y2=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        return(self.x1,self.y1,self.x2,self.y2)
    def Vector2_points(self,x1=0,y1=0,x2=0,y2=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        return(self.x1,self.y1,self.x2,self.y2)
# finding distance between two points of vector 1
    def dictance1(self):
        global d1
        d1=math.sqrt((self.x2-self.x1)**2)+((self.y2-self.y1)**2)
        return("The Distance between two point of vector1 is {}".format(d1)) 
        
# finding distance between two points of vector 2           
    def dictance2(self):
        global d2
        d2=math.sqrt((self.x2-self.x1)**2)+((self.y2-self.y1)**2)
        return("The Distance between two point of vector2 is {}".format(d2)) 
       
# finding Its Resultant vector
    def resultant_vector(self):
        R=math.sqrt((d1)**2)+((d2)**2)
        return("The Resultant vector is {}".format(R))
V=vector()
print(V.Vector1_points())
print(V.Vector2_points())
print(V.dictance1())
print(V.dictance2())
print(V.resultant_vector())       
#------------------------------------------------------------------------------------------------
#Task 2
class courses:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
    def detail(self):
        return("The subject name is {} and the subject instructor is {}\n".format(self.name,self.teacher))
    
class pf(courses):
    def ch(self,credithours):
        self.credithours=credithours
        return("{} require {} credit hours for pass\n".format(self.name,self.credithours))
class pf_labs(pf):
    def lab(self,credithours):
        self.credithours=credithours
        return("if you pass the subject {}  then you will be pratice more  in lab of pf subject and you give {} credithours to pass \n".format(self.name,self.credithours))
        
class oops(pf_labs):
    def appearence(self,subject):
        self.subject=subject
        return("you will be appeare in {} subject if you will pass the {} subject  and it lab exam in first semester otherwise you will repeate the first semester \n".format(self.subject,self.name))
            
        
sub=oops("pf","sirfaisal")
print(sub.detail())
print(sub.ch("2 hours daily"))        
print(sub.lab("1 hours for pratice"))
print(sub.appearence("OOPS"))
#---------------------------------------------------------------------------------------------------
#task 3:
class Book:
    def __init__(self,title,author,translator,published,ISBN):
        self.title=title
        self.author=author
        self.translator=translator
        self.published=published
        self.ISBN=ISBN
        
    def About_book(self,Main_characters):
        self.Main_characters=Main_characters
        return(f"The original title of the book is {self.title}\n"\
               f"The author of the book is{self.author}\n" \
               f"The translator of this book is{self.translator}\n"\
               f"This book was published in {self.published}\n"\
               f"The ISBN number is {self.ISBN}\n"
               f"The main characters of the story are {self.Main_characters}\n")
class pages(Book):
    def numbers(self,pages):
        self.pages=pages
        return("This book contain {} pages \n".format(self.pages))
class chapter(pages):
    def index(self,ind_number):
        self.ind_number=ind_number
        return("this books has {} plays \n".format(self.ind_number))  
class Exercise(chapter):
    def exer(self,type_of_book):
        self.type_of_book=type_of_book
        return("this books is {} soo it has no exercise init \n".format(self.type_of_book))
class tasks(Exercise):
    def tsk(self):
        return ("this books is a novel soo this Book contain no exercise")        
obj=tasks("Le Comte de Monte-Cristo"," Alexandre Dumas"," Robin Buss","Published May 27th 2003 by Penguin Classics (first published 1844)"," (ISBN13: 9780140449266)")
print(obj.About_book("[CharactersEdmond Dantès,\n Abbé Faria,\n Giovanni Bertuccio,\n Luigi Vampa,\n Haydée,\n Mercédès Mondego,\n Fernand Mondego,\n Albert de Morcerf,\n Baron Danglars, \n,Gérard de Villefort,\n Valentine de Villefort,\n Noirtier de Villefort,\n Héloïse de Villefort,\n Pierre Morrel,\n Maximilien Morrel,\n Beauchamp,\n Franz d'Épinay,\n Lucien Debray,\n Eugénie Danglars,\n Hermine Danglars,\n Benedetto, Kadrus ]"))
print(obj.numbers(1276))
print(obj.index(12))
print(obj.exer("Historical Novel"))
print(obj.tsk())
#---------------------------------------------------------------------------------------------------
#Task 4
class family:
    def introo1(self):
        return("This is our Family tree")
class Grand_father(family):
    grandfather=""
    def introo2(self):
        return(f"This is my {self.grandfather} grandfather and he is trader_Of_soul") 
class Grand_mother(family):
    grandmother=""
    def introo3(self):
        return(f"This is my {self.grandmother} grandmother and she is a housewife")
class son1_of_Grand_father(Grand_father,Grand_mother):
    bharayabba1=""
    def introo4(self):
        return(f"This is my {self.bharayabba1} bharaypaa big_son of my grandfather")
class son2_of_Grand_father(Grand_father,Grand_mother):
    bharayabba2=""
    def introo5(self):
        return(f"This is my {self.bharayabba2} second_bharaypaa big_son of my grandfather")        
class son3_of_Grand_father(Grand_father,Grand_mother):
    bharayabba3=""
    def introo6(self):
        return(f"This is my {self.bharayabba3} third_bharaypaa big_son of my grandfather")        
class Father(Grand_father,Grand_mother):
    father=""
    def introo7(self):
        return(f"This is my {self.father} father_son of my grandfather")
class Mother(family):
    mother=""
    def introo8(self):
        return(f"This is my {self.mother} wife of my father")
class Me(Father,Mother):
    me=""
    def introo9(self):
        return(f"My name is {self.me} and I am son of {self.father} and {self.mother}")
M1=Me()
M1.grandfather=" Mr Naeem_uddin_siddique"
M1.grandmother="Mrs Naseem_uddin_siddique"
M1.father="Mr sohail_uddin_siddique"
M1.mother="Mrs nazia_siddique"
M1.me="Huzaifa_siddique"
s1=son1_of_Grand_father()
s1.bharayabba1="Mr faheem_uddin_siddique"
s2=son2_of_Grand_father()
s2.bharayabba2="Mr waseem_uddin_siddique"
s3=son3_of_Grand_father()
s3.bharayabba3="Mr yaseen_uddin_siddiue"
print(M1.introo1())
print(s1.introo4())
print(s2.introo5())
print(s3.introo6())       
print(M1.introo2())
print(M1.introo3())
print(M1.introo7())
print(M1.introo8())
print(M1.introo9())            
#-------------------------------------------------------------------------------------------
# Create classes of RAM, HD, Graphics Cards, Processors and used it in your customize laptop.
class System:
    print("This is a system")
class RAM(System):
    def type(self,type_of_ram):
        self.type_of_ram=type_of_ram
        return(f"The system contain {self.type_of_ram}")
class HD(System):
    def video_mode(self,v_mode,pixcels,scanning_mode):
        self.v_mode=v_mode
        self.pixcels=pixcels
        self.scanning_mode=scanning_mode
        return(f"The system contain {self.v_mode} frame size in {self.pixcels} and mode of scanning is {self.scanning_mode}")

class Graphic_card(System):
    def G_c(self,type_of_card):
        self. type_of_card=type_of_card
        return(f"The  system contain  {self.type_of_card}  Graphic card")           
        
class Processor(System):
    def Pro(self,type_of_processor):
        self.type_of_processor=type_of_processor
        return(f"The system was {self.type_of_processor}")
class Laptop(RAM,HD,Graphic_card,Processor):
    def intro(self):
        return(f"the system has "
               f"{self.type_of_ram} Ram"
               f"{self.v_mode} HD"
               f"{self.type_of_card} Graphic card"
               f"{self.type_of_processor}  Proceseeor")  
l=Laptop()
print(l.type("DIMM")) 
print(l.video_mode("720","1280x720","progressive"))
print(l.G_c("Integrated Craphic card"))
print(l.Pro("Pentium 4"))  
print(l.intro())

#------------------------------------------------------------------------------------------------------------------
    


