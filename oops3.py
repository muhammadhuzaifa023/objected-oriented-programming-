# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:31:58 2020

@author: HASSAN ENTERPRISES
"""
# oops mini project library management 
            
            
        
#--------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
class cargo:
    print("this cargomangement system")
class cargo_database(cargo):
    def __init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data):
        self.sender_data=sender_data
        self.receiver_data=receiver_data
        self.cargo_record=cargo_record
        self.employee_data=employee_data
        self.driver_data=driver_data
    def senderdetail(self):
        print(self.sender_data)
    def receiverdetail(self):
        print(self.receiver_data)
    def employeedetail(self):
        print(self.employee_data)
    def driverdata(self):
        print(self.driver_data)
class sender(cargo_database):
    def __init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data,name,phonenumber,cargo_id,cnic_number):
        cargo_database .__init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data)       
        self.name=name
        self.phonenumber=phonenumber
        self.cargo_id=cargo_id
        self.cnic_number=cnic_number
    def booked_cargo(self):
        return('The name of sender is {} his cnic is {} and his phone no is {} and his cargo_id is {}'.format(self.name,self.cnic_number,self.phonenumber,self.cargo_id))

class Employee(cargo_database):
    def __init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data,name,phone_number):
       cargo_database .__init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data)     
       self.name=name
       self.phone_number=phone_number
    def  cargo_detailed(self):
         return("The sendermail record are {} \n The recevierrecord are {}\n The cargorecord are {} and the driver data{}".format(self.sender_data,self.receiver_data,self.cargo_record, self.driver_data))
class cargo_receiver(Employee):
     def __init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data,name,phone_number,Receiver_name,Receiver_phone_number,cnic_number,cargo_number):
         cargo_database .__init__(self,sender_data,receiver_data,cargo_record,employee_data,driver_data)
         self.Receiver_name=Receiver_name
         self.Receiver_phone_number=Receiver_phone_number
         self.cnic_number=cnic_number
         self.cargo_number=cargo_number
     def received_cargo(self):
         return(self.Receiver_name,self.Receiver_phone_number,self.cnic_number,self.cargo_detailed)
    
receiver=cargo_receiver(["Muhammadhuzaifa\n Muhamamd Bilal \n Muhammad safi"],["muhammad saad","safi uddin"],["cars"],["zubair","asad","faraz","shoaib"],"##","Ajaz","03360213796","sohail","03158287251","2353644745885959","56321")
sen=sender(["Muhammadhuzaifa\n Muhamamd Bilal \n Muhammad safi"],["muhammad saad","safi uddin"],["cars"],["zubair","asad","faraz","shoaib"],"##","Ajaz","03360213796","456789","74278723232")
print(receiver.senderdetail())
print(receiver.receiverdetail())
print(receiver.employeedetail())
print(receiver.driverdata())
print(sen.booked_cargo())
print(receiver.cargo_detailed())
print(receiver.received_cargo())



#---------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
# Driver code
R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()
#-------------------------------------------------------------------------------------------
from abc import ABC ,abstractmethod
class polygon(ABC):
    @abstractmethod
    def no_of_side(self):
        pass
class square(polygon):
    def no_of_side(self):
        return("I have 4 sides")
class triangle(polygon):
    def no_of_side(self):
        return("I have 3 sides")
sq=square()
print(sq.no_of_side())    
#-----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
class university(ABC):
    @abstractmethod
    def university_name(self):
        pass
    def department_name(self):
        pass
class student(university):
    def university_name(self):
        return("My university name is uit")
    def department_name(self):
        return("The department name is CS")
st=student()
print(st.university_name())
print(st.department_name())    
#-------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
class Person(ABC):
    def ShowName(self):
        print("Abstract Base Class")
class Student(Person):
    def ShowName(self):
        super().ShowName()
        print("subclass ")
# Driver code
S1 = Student()
S1.ShowName()
#--------------------------------------------------------------------------------------------
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def Account_name(self):
        pass
    def Rate_of_interest(self):
        pass
    def Deposit(self):
        pass
    def Withdraw(self):
        pass
class HBL(Bank):
    def Account_name(self,accountname):
        self.accountname = accountname
        print('Please enter your account name = {}'.format(self.accountname))
    def Rate_of_interest(self,rateofinterest):
        self.rateofinterest = rateofinterest
        print('The rate of interest for the bank is = {}'.format(self.rateofinterest))
    def Deposit(self,deposit):
        self.deposit = deposit
        print('The deposit amoont for the cash is =  {}'.format(self.deposit))
class Bank():
    pass
class Meezan(Bank):
    def Account_name(self,accountname):
        self.accountname = accountname
        print('Please tell your account name {}'.format(self.accountname))
    def Rate_of_interest(self,rateofinterest):
        self.rateofinterest = rateofinterest
        print('The rate of interest for the bank is = {}'.format(self.rateofinterest))
    def Deposit(self,deposit):
        self.deposit = deposit
        print('The deposit amount for the cash is {}'.format(self.deposit))
    def Withdraw(self,withdraw):
        self.withdraw = withdraw
        print('The amount you want to widthdraw is {}'.format(self.withdraw))
class Alfalah(Bank):
    def Account_name(self,accountname):
        self.accountname = accountname
        print('Please tell your account name {}'.format(self.accountname))
    def Rate_of_interest(self,rateofinterest):
        self.rateofinterest = rateofinterest
        print('The rate of interest for the bank is {}'.format(self.rateofinterest))
    def Deposit(self,deposit):
        self.deposit = deposit
        print('The deposit amoont for the cash is {}'.format(self.deposit))
    def Withdraw(self,withdraw):
        self.withdraw = withdraw
        print('The amount you want to widthdraw is {}'.format(self.withdraw))
class Habibmetro(Bank):
    def Account_name(self,accountname):
        self.accountname = accountname
        print('Please tell your account name {}'.format(self.accountname))
    def Rate_of_interest(self,rateofinterest):
        self.rateofinterest = rateofinterest
        print('The rate of interest for the bank is {}'.format(self.rateofinterest))
    def Deposit(self,deposit):
        self.deposit = deposit
        print('The deposit amoont for the cash is {}'.format(self.deposit))
    def Withdraw(self,withdraw):
        self.withdraw = withdraw
        print('The amount you want to widthdraw is {}'.format(self.withdraw))
        
f=HBL()
f.Account_name('Zohair')
f.Rate_of_interest('2.4%')
f.Deposit('45000')

t=Meezan()
t.Account_name('Tahir')
t.Deposit('63000')
t.Rate_of_interest('5.2%')

t.Withdraw('12000')

#---------------------------------------------------------------------------------------------
class Butterfly:
    pass
class BlueMorpho(Butterfly):
    def Info(self):
        print('They are the most rare butterflies. They are 1 out of thirty their time is mostly spent reproducing')
    def color(self):
        print('The color of this butterfly is dark blue')
    def Pattern(self):
        print('The butterfly wings are blue but they are black at the ends')
    def origin(self):
        print('They are basically found in Latin America Tropical forests in California')
    def life_span(self):
        print('The lifespan of blue morpho butterfly is 115 days')
class JanettaForester(Butterfly):    
    def Info(self):
        print('They are the most colorful butterflies. They are they are listed to be 180 species')
    def color(self):
        print('The color of this butterfly are multi')
    def Pattern(self):
        print('The butterfly wings are blue,yellow and black in color')
    def origin(self):
        print('They are basically found in the African Continent')
    def life_span(self):
        print('The lifespan of Janetta Forester butterfly is unknown')
class Swallowtail(Butterfly):
    def Info(self):
        print('Swallowtail butterflies are large, colorful butterflies in the family Papilionidae, and include over 550 species')
    def color(self):
        print('Colour patterns may vary, although many species have yellow, orange, red, green, or blue markings on an iridescent black, blue, or green background.')
    def Pattern(self):
        print('The butterfly wings are blue,yellow and black in color with leaf pattern on them')
    def origin(self):
        print('The majority of swallowtail species and the greatest diversity are found in the tropics and subtropical regions')
    def life_span(self):
        print('The lifespan of swallowtail butterfly is about 10 to 12 days.')

sub1=BlueMorpho()
sub2=JanettaForester() 
sub3=Swallowtail()

for butterfly in (sub1,sub2,sub3):
   butterfly.Info()
   butterfly.color()
   butterfly.Pattern()
   butterfly.origin()
   butterfly.life_span()
#----------------------------------------------------------------------------------------------
from abc import ABCMeta,abstractmethod 
class Bank(metaclass=ABCMeta):
    @abstractmethod
    #def Account_name(self):
        #pass
    #def Rate_of_interest(self):
        #pass
    def deposite(self,amount):
        pass
    def withdraw(self,amount):
        pass
class Bank_AlHabib(Bank):
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        return("You deposit an amount of Rs {}".format(self.balance))
    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance=self.balance-amount
            return("You withdraw an amount of Rs {}".format(self.balance))
        else:
            print("Insufficient funds")
    def print_balance(self):
         return(self.balance)
class Bank_HabibMetro(Bank):
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        return("You deposit an amount of Rs {}".format(self.balance))
    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance=self.balance-amount
            return("You withdraw an amount of Rs {}".format(self.balance))
        else:
            print("Insufficient funds")
    def print_balance(self):
         return(self.balance)
class Bank_Mezan(Bank):
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        return("You deposit an amount of Rs {}".format(self.balance))
    def withdraw(self,amount):
        if (self.balance>=amount):
           self.balance=self.balance-amount
           return("You withdraw an amount of Rs {}".format(self.balance))
        else:
            print("Insufficient funds")
    def print_balance(self):
         return(self.balance)
class Bank_AlFalah(Bank):
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        return("You deposit an amount of Rs {}".format(self.balance))
    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance=self.balance-amount
            return("You withdraw an amount of Rs {}".format(self.balance))
        else:
            print("Insufficient funds")
    def print_balance(self):
         return(self.balance)         
account1=Bank_AlHabib()
account2=Bank_HabibMetro()
account3=Bank_Mezan()
account4=Bank_AlFalah()
while(True):
    print("In which of the following you have an account")
    print("1)   Bank-AlHabib")
    print("2)   Bank-HabibMetro")
    print("3)   Bank-Mezan")
    print("4)   Bank-AlFalah")
    user_choice=input()
    if user_choice not in ["1","2","3","4"]:
            print("Please enter a Valid Option")
            continue
    else:
            user_choice=int(user_choice)
    if user_choice ==1:
            #lib.displaybook()
            print("Do you want to deposit the ammount in Bank-AlHabib")
            print("or")
            print("Do you want to withdraw the amount in Bank-AlHabib")
            a=input("If you want to deposit than put YES in this form or If you want to withdraw than put yes in this form")
            if a=="YES":
                print("How many ammount you want to deposit..?")
                amount=int(input("Enter the amount you want to deposit"))
                print(account1.deposite(amount))
                print(account1.print_balance())
            elif a=="yes":
                print("How many amount you want to withdraw...?")
                amount=int(input("Enter the amount you want to withdraw"))
                print(account1.withdraw(amount))
                print(account1.print_balance())
                
            else:
                print("Not a valid option")
            
    elif user_choice ==2:
            print("Do you want to deposit the ammount in Bank-HabibMetro")
            print("or")
            print("Do you want to withdraw the amount in Bank-HabibMetro")
            a=input("If you want to deposit than put YES in this form or If you want to withdraw than put yes in this form")
            if a=="YES":
                print("How many ammount you want to deposit..?")
                amount=int(input("Enter the amount you want to deposit"))
                print(account1.deposite(amount))
                print(account1.print_balance())
            elif a=="yes":
                print("How many amount you want to withdraw...?")
                amount=int(input("Enter the amount you want to withdraw"))
                print(account1.withdraw(amount))
                print(account1.print_balance())
                
            else:
                print("Not a valid option")
            
    elif user_choice ==3:
            print("Do you want to deposit the ammount in Bank-Mezan")
            print("or")
            print("Do you want to withdraw the amount in Bank-Mezan")
            a=input("If you want to deposit than put YES in this form or If you want to withdraw than put yes in this form")
            if a=="YES":
                print("How many ammount you want to deposit..?")
                amount=int(input("Enter the amount you want to deposit"))
                print(account1.deposite(amount))
                print(account1.print_balance())
            elif a=="yes":
                print("How many amount you want to withdraw...?")
                amount=int(input("Enter the amount you want to withdraw"))
                print(account1.withdraw(amount))
                print(account1.print_balance())
                
            else:
                print("Not a valid option")
            
    elif user_choice ==4:
            print("Do you want to deposit the ammount in  Bank-AlFalah")
            print("or")
            print("Do you want to withdraw the amount in  Bank-AlFalah")
            a=input("If you want to deposit than put YES in this form or If you want to withdraw than put yes in this form")
            if a=="YES":
                print("How many ammount you want to deposit..?")
                amount=int(input("Enter the amount you want to deposit"))
                print(account1.deposite(amount))
                print(account1.print_balance())
            elif a=="yes":
                print("How many amount you want to withdraw...?")
                amount=int(input("Enter the amount you want to withdraw"))
                print(account1.withdraw(amount))
                print(account1.print_balance())
                
            else:
                print("Not a valid option")
            
    else:
            print("Not a Valid Option")
    print("Press q to quit and c to continue") 
    user_choice2=""
    while(user_choice2 !="c"and user_choice2 !="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            if user_choice2 =="c":
                continue        
       

   
                
            
            
            
            
            
            
            
            
            
            