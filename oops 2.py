# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:43:15 2020

@author: HASSAN ENTERPRISES
"""
#---------------------------------------------------------------------------------------------------
class Airline_travellers:
    def __init__(self,foodservice="Normal",cost="37000/="):
        self.foodservice=foodservice
        self.cost=cost
    def fuel1(self):
        return("In domestic flight we have the {} food_service and it cost is {}".format(self.foodservice,self.cost))
class Businessclass:
    def fuel2(self,foodservice,cost,facility):
        self.foodservice=foodservice
        self.cost=cost
        self.facility=facility
        return("In business flight we have the {} food_service and it cost is {} with fully  {} ".format(self.foodservice,self.cost,self.facility))       
class VIPclass(Airline_travellers,Businessclass):
       def fuel3(self,foodservice="luxiorous",cost="100,000/=",facility="A.C compartment"):
        self.foodservice=foodservice
        self.cost=cost
        self.facility=facility
        return("In VIPClass flight we have the {} food_service and it cost is {} with fully  {} ".format(self.foodservice,self.cost,self.facility))   
     
Al=VIPclass()
print(Al.fuel1())
print(Al.fuel2("luxiours","70,000/=","A.C compartment"))
print(Al.fuel3())
        
#-------------------------------------------------------------------------------------------------
class MS_Word:
    version=""
    def __init__(self,Maximum_number_of_BOOKsMarks,maximum_number_of_styles,Maximum_number_of_lists,Maximum_number_of_comments,Maximum_number_of_moves):
        self.Maximum_number_of_BOOKsMarks=Maximum_number_of_BOOKsMarks
        self.maximum_number_of_styles=maximum_number_of_styles
        self.Maximum_number_of_lists=Maximum_number_of_lists
        self.Maximum_number_of_comments=Maximum_number_of_comments
        self.Maximum_number_of_moves=Maximum_number_of_moves
    def Version(self):
        return("In {} version of MS we have the following things in {} and{} and {} and{}and{}".format(self.version,self.Maximum_number_of_BOOKsMarks,self.maximum_number_of_styles,self.Maximum_number_of_lists,self.Maximum_number_of_comments,self.Maximum_number_of_moves))
    
class Home(MS_Word):
    def cut(self):
        return("Throught cut we have to cut the page")
    def copy(self):
        return("Throught copy we have to copy the content")
    def paste(self):
        return("Throught paste we have to paste the content")
    def font(self):
        return("Through font we can change the fontsize")
    def style(self):
        return("Through Style we can Style our Heading")
class Insert(MS_Word):
    def pages(self,material):
        self.material=material
        return("Through pages Ms_words give us {}".format(self.material))
    def Table(self,material):
        self.material=material
        return("Through Tables we can draw the {}".format(self.material))
    def Illustration(self,material):
        self.material=material
        return("In MS_word Illustration provide us {} service".format(self.material))
    def Media(self,material):
        self.material=material
        return("In MS_word Media provide us {}".format(self.material))
class Layout(MS_Word):
    def Pages_setup(self,material):
        self.material=material
        return("In MS_word Pages_setup gives us {}".format(self.material))
    def Paragraph(self,material):
        self.material=material
        return("In MS_word paragraph gives us {}".format(self.material))
h=Home("2,147,483,647","4,079","2,047","2,147,483,647","2,147,483,647")
h.version="2007"
print(h.Version())        
print(h.cut())
print(h.copy())
print(h.paste()) 
print(h.font())
print(h.style()) 
I=Insert("2,147,483,647","4,079","2,047","2,147,483,647","2,147,483,647")
I.version="2009"
print(I.pages("[coverpage,blankpage,Pagebreak]"))
print(I.Table("Table"))
print(I.Illustration("[Picture,Online_picture,Shape,Smartart,chart,ScreenShort]"))
print(I.Media("Online_Video") ) 
L=Layout("2,147,483,647","4,079","2,047","2,147,483,647","2,147,483,647")
L.Pages_setup("[margin,orientation,size,column,Breaks,LineNumbers,Hyphenation]")
L.Paragraph("[Indent,Spacing]")
#-------------------------------------------------------------------------------------------------------
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        return (self.length*self.width)
    def perimeters(self):
        return 2*self.length+2*self.width
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
sq=Square(6)
print(sq.Area() )  

#-----------------------------------------------------------------------------------------------------------------
class Engine:
    def __init__(self,Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output):
        self.Basic_engine_model=Basic_engine_model
        self.Number_of_cylinder=Number_of_cylinder
        self.Compression_Ratio=Compression_Ratio
        self.Maximum_power_output=Maximum_power_output
    def Move_UP_down1(self):
        return("Every Engine depand on such things")
    def Move_left_right2(self):
        return( "Here the EngineModel is{} and its cylinder_number is {} and its compression Ratio is{} and its maximum output power{}".format(self.Basic_engine_model,self.Number_of_cylinder,self.Compression_Ratio,self.Maximum_power_output))
class Thermal_Engine(Engine):
    name=""  
    def __init__(self,Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output):
        super().__init__(Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output)
    def Move_UP_down3(self):
        return("We have such types of Engines in Thermal Engine {}".format(self.name))
class Ic_Engine(Thermal_Engine):
    def __init__(self,Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output,Fuel_Air_Ratio,Specific_Output,Thermal_Efficiency_and_Heat_Balance,Exhaust_Smoke_and_Emissions,Effective_Pressure_and_Torque):
        super().__init__(Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output)
    #def __init__(self,Fuel_Air_Ratio,Specific_Output,Thermal_Efficiency_and_Heat_Balance,Exhaust_Smoke_and_Emissions,Effective_Pressure_and_Torque):
        self.Fuel_Air_Ratio=Fuel_Air_Ratio
        self.Specific_Output=Specific_Output
        self.Thermal_Efficiency_and_Heat_Balance=Thermal_Efficiency_and_Heat_Balance
        self.Exhaust_Smoke_and_Emissions=Exhaust_Smoke_and_Emissions
        self.Effective_Pressure_and_Torque=Effective_Pressure_and_Torque
    def Move_UP_down5(self):
        return("In IC Engines include BUS engine,train engine,Airoplane engine")
    def Move_left_right6(self):
        return("The major components of IC Engine is Fuel Ratio {},Thermal_Efficiency {} smoke emulsion {} Breaking Torque {}".format(self.Fuel_Air_Ratio,self.Specific_Output,self.Thermal_Efficiency_and_Heat_Balance,self.Exhaust_Smoke_and_Emissions,self.Effective_Pressure_and_Torque))
class EC_Engine(Thermal_Engine):
    def __init__(self,Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output,Boilier,Piston_turbine,Thermodynamic_Combuction,Regenerator_power_output):
        super().__init__(Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output)
        self.Boilier=Boilier
        self.Piston_turbine=Piston_turbine
        self.Thermodynamic_Combuction=Thermodynamic_Combuction
        self.Regenerator_power_output=Regenerator_power_output
    def Move_Up_down7(self):
        return("EC Engine used in Industrical working")
    def Move_left_right8(self):
        return("The major components of EC Engine is {} Boilier {} turbine Thermodynamic_Compresshion {} and Regenerator_power_output {}".format(self.Boilier,self.Piston_turbine,self.Thermodynamic_Combuction,self.Regenerator_power_output))
class Reaction_Engine(Thermal_Engine):
    def __init__(self,Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output,combutionspeed,gas_injection_ratio):
        super().__init__(Basic_engine_model,Number_of_cylinder,Compression_Ratio,Maximum_power_output)
        self.combutionspeed=combutionspeed
        self.gas_injection_ratio=gas_injection_ratio
    def Move_up9(self):
        return("reactions Engines used in Rocket and fighterjets and its majors components are {} and {}".format(self.combutionspeed,self.gas_injection_ratio))
        
Ic= Ic_Engine("Caterpillar4078","2","16.25:1","74.6Kw(2100rpm)","56%","87%","56%","30%","100%")
Ic.name="[ICengine,ECengine,Reactionengine]"     
print(Ic.Move_UP_down1())       
print(Ic.Move_left_right2())        
print(Ic.Move_UP_down3())
print(Ic.Move_UP_down5())
print(Ic.Move_left_right6())       
Ec=EC_Engine("Caterpillar4078","2","16.25:1","74.6Kw(2100rpm)","aliminium","34housepower","Quiescent","70%")
print(Ec.Move_Up_down7())
print(Ec.Move_left_right8())        
Re=Reaction_Engine("Caterpillar4078","2","16.25:1","74.6Kw(2100rpm)","combuctionspeed","gas inject ratio")        
print(Re.Move_up9())        
        
        
#---------------------------------------------------------------------------------------------------------------
class Boy:
    name ="" 
    gender ="Male" 
    age = 20
class Girl:
    name =""
    gender ="Female" 
    age = 18
Irtiza = Boy() 
Ahmed = Boy() 
Arisha = Girl() 
Ayesha = Girl()
print("My name is : " + "Irtiza") 
Irtiza.gender 
print(Irtiza.gender)
Irtiza.age = 21 
print(Irtiza.age)        
#------------------------------------------------------------------------------------------------------------------------
class parent:
    def __init__(self):
        self.classvar="I am from class parent constructor"
        self.name="My name is huzaifa"
class Child(parent):
    #Instance variable
     def __init__(self):
         super().__init__()
     #def __init__(self):
         self.classvar="I am form child constructor"
# Instance object         
x=Child()
print(x.classvar)                 
print(x.name)       
#------------------------------------------------------------------------------------------------------------------
#case study 1
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id):
        super().__init__(name,id)
    def Python_programmer(self):
        return(self.name,self.id)
p=Programmer("Huzaifa","021")
print(p.Python_programmer())        
#--------------------------------------------------------------------------------------------------------------------
#case study 2
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Detail(self):
        return("Employee Data Name age and post is ",self.name,self.age)
class programmer:#yahan pr programmer ek dusarii class haii joo inherit haii upper walii class say likin 
    #eska oject ki help say may nay upper wali class ka attributes koo call kiyaaa
    def __init__(self,salary,prolang,exp):
        self.salary=salary
        self.prolang=prolang
        self.experience=exp
    def Details(self):
        return(self.salary,self.prolang,self.experience)
class Designer(Employee,programmer):
    def __init__(self,name,age,salary,prolang,exp):
        Employee.__init__(self,name,age)
        programmer.__init__(self,salary,prolang,exp)
D=Designer("Muhammad",20,440000,"python","5-Year")
print(D.Details()) 
print(D.Detail())      
#----------------------------------------------------------------------------------------------------------------
        
#--------------------------------------------------------------------------------------------------------------------------------------------
class Classic_Umbrella:
    def __init__(self,material,style,prints,size,used_for):
        self.material=material
        self.style=style
        self.prints=prints
        self.size=size
        self.used_for=used_for
    def ForRain(self):
        return("This is the most common type of modern foldable umbrellas. Commonly made with {} to keep the rain off, these umbrellas are your everyday portable shelters from storms.Its style is {} and its printing is{} Its size is {}.This Umbrella is used for Both {} \n".format(self.material,self.style,self.prints,self.size,self.used_for))        
class Bubble_Umbrella:
    def __init__(self,fmaterial,fstyle,fprints,fsize,fused_for):
        self.fmaterial=fmaterial
        self.fstyle=fstyle
        self.fprints=fprints
        self.fsize=fsize
        self.fused_for=fused_for
    def ForSunprotection(self,colors):
        self.fcolors=colors
        return("This is the most commmon type of foldable umbrella.commonly made up of {} to Sunprotection and rainfalls.These are great for {} who love to peer out at the rain while keeping their faces dry.Its style is {} and its printing is{} Its size is {}.Its has diffrents colos {}".format(self.fmaterial,self.fused_for,self.fstyle,self.fprints,self.fsize,self.fcolors))        
       
class Automatic_Umbrella(Classic_Umbrella,Bubble_Umbrella):
    def __init__(self,material,style,prints,size,used_for,fmaterial,fstyle,fprints,fsize,fused_for):
        Classic_Umbrella.__init__(self,material,style,prints,size,used_for)
        Bubble_Umbrella.__init__(self,fmaterial,fstyle,fprints,fsize,fused_for)
    
AU=Automatic_Umbrella("metal of polyesther shafts with microfiber fabric canopys","Classic","Screenprinting","20 to 40 inches","Adults and kids","clear plastic","Kids","Bubble","Digital printing","20 to 40 inches")
print(AU.ForRain())
#AH=Automatic_Umbrella("clear plastic","Kids","Bubble","Digital printing","20 to 40 inches")
print(AU.ForSunprotection("[red,green,blue]"))

#Making an abstract class
#----------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
class Vehicle(ABC):
    '''This class inherits from (or subclasses) ABC'''
    
    @abstractmethod
    def number_of_wheels(self):
        '''This method is abstract, so the class cannot be instantiated. This method will be overridden in subclasses of Vehicle.'''
        pass
class Car(Vehicle):
    '''This class inherits from the abstract base class Vehicle'''
    def number_of_wheels(self):
        '''Override the abstract method in the base class'''
        return 4
# create a car called c: SUCCEEDS
c = Car() 
# print the number of wheels that c has: SUCCEEDS
print(c.number_of_wheels()) 
# Try to create a Vehicle: FAILS
v = Vehicle()

#-----------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod 

class Polygon(ABC): 

	# abstract method 
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

#------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod 
class Animal(ABC): 
  
    def move(self): 
        pass
  
class Human(Animal): 
  
    def move(self): 
        print("I can walk and run") 
  
class Cat(Animal): 
  
    def move(self): 
        print("I can run, I can play") 
  
class Dog(Animal): 
  
    def move(self): 
        print("I can helps, I can play") 
  
class Lion(Animal): 
  
    def move(self): 
        print("I can run very fast, I can hunt") 

#--------------------------------------------------------------------------------------------------------
from abc import ABCMeta,abstractmethod 
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
        
class Rectangle(Shape):
    types="Rectangle"
    sides =4
    def __init__(self):
        self.length=6
        self.width=4
    def printarea(self):
        return(self.length*self.width)
rect1=Rectangle()        
print(rect1.printarea())        
#-----------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
 
 
class AbstractOperation(ABC):
 
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()
    
    @abstractmethod
    def execute(self):
        pass
class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b
 
 
class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b
 
 
class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operand_a * self.operand_b
 
 
class DivideOperation(AbstractOperation):
    def execute(self):
        return self.operand_a / self.operand_b
    
op_add = AddOperation (5,10)
print(op_add.execute())  
op_sub = SubtractOperation(10,5)
print(op_sub.execute())
op_mul = MultiplyOperation(5,7)
print(op_mul.execute())
op_div = DivideOperation(75,5)
print(op_div.execute())  
#-------------------------------------------------------------------------------------------------------------
from abc import ABCMeta,abstractmethod 
class Robot(metaclass=ABCMeta):
    @abstractmethod
    def orders(self):
        pass
    def cleaning(self):
        pass
class cookerRobo(Robot):
    def orders(self):
        return("My Robots Follows All my orders")
    def cleaning(self):
        return("My Robots is a good cleaning master")
    def cooking(self):
        return("My Robot is a good cooker")
class GardnerRobo(Robot):
    def orders(self):
        return("My Robots Follows All my orders")
    def cleaning(self):
        return("My Robots is a good cleaning master")
    def waterplants(self):
        return("My robot watering the plants on time")
co=cookerRobo()
print(co.orders())
print(co.cleaning())       
print(co.cooking())
Ga=GardnerRobo()
print(Ga.orders())
print(Ga.cleaning())
print(Ga.waterplants())
#-----------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod   
class Polygon(ABC): 
 
    # abstract method 
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
        
#------------------------------------------------------------------------------------------------------------------
first = 54
second = 89
total = first + second
print("Total sum of both :", total)
#---------------------------------------------------------------------------------------------------------------------
first = 'Usman Institute of '
second = 'Technology'
total = first + second
print("The concatinated form of both variable is :", total)
#-------------------------------------------------------------------------------------------------------------------
print(len("Syed Faisal Ali"))
print(len(["Usman", "Institite",  "of ", "Technology"]))
print(len({"Name": "Ahmed", "Address": "Gulshan", "Qualification":"BSCS"}))
#------------------------------------------------------------------------------------------------------------------
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat_1 = Cat("Tom", 2.5)
dog_1 = Dog("Scobby", 4)

for animal in (cat_1, dog_1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
        
 #-------------------------------------------------------------------------------------------------------------------       
# polymorphism mean derived from two word 
# poly and morphism poly ka matlan many and morphism mean differents forms

class Shark():
    def swim(self):
        print("The shark is swimming.")
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")
class Clownfish(): 
    def swim(self):
        print("The clownfish is swimming.")
    def swim_backwards(self):
        print("The clownfish can swim backwards.")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")
# initiate the classes into two objects:
...
Obj_shark = Shark() 
print(Obj_shark.skeleton())
Obj_clownfish = Clownfish() 
print(Obj_clownfish.skeleton())
#---------------------------------------------------------------------------------------------------------------------------
#Another way of calling objects
for i in (Obj_shark,Obj_clownfish):
    i.swim_backwards()
    i.skeleton()
#-----------------------------------------------------------------------------------------------------------------------------
from abc import ABCMeta,abstractmethod 
class fish(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass
    def swim_backwards(self):
        pass
    def skeleton(self):
        pass
class Shark(fish):
    def swim(self):
        print("The shark is swimming.")
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")
class Clownfish(fish): 
    def swim(self):
        print("The clownfish is swimming.")
    def swim_backwards(self):
        print("The clownfish can swim backwards.")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")
Obj_shark = Shark() 
Obj_clownfish = Clownfish()
for fish in (Obj_shark,Obj_clownfish):
    fish.swim_backwards()
    fish.skeleton()
#------------------------------------------------------------------------------------------------------------------
class Tomato:
    def type(self):
        print("This is tomato")
    def color(self):
        print("It color is red")
class Apple:
    def type(self):
        print("This is Apple")
    def color(self):
        print("It color is red")
def calling(obj):
    obj.type()
    obj.color()
blu=Tomato()
peggy=Apple()
calling(blu)
calling(peggy)        
#-----------------------------------------------------------------------------------------------------------
class Parrot:
    def fly(self): 
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim") 
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self): print("Penguin can swim")
# common interface 
def flying_test(bird):
    bird.fly()
#instantiate objects
 
blu = Parrot() 
peggy = Penguin()
# passing the object 
flying_test(blu) 
flying_test(peggy)   
#-------------------------------------------------------------------------------------------------------------------
class Tomato:
    def type(self):
        print("This is tomato")
    def color(self,color):
        self.color=color
        print("It color is {}".format(self.color))
class Apple:
    def type(self):
        print("This is Apple")
    def color(self):
        print("It color is r{}".format(self.color))
def calling(obj):
    obj.type()
    obj.color("color")
blu=Tomato()
peggy=Apple()
calling(blu)
calling(peggy)   
#--------------------------------------------------------------------------------------------------------------------
import math
class Rectangle:
    def int (self, color, filled, width, length): 
        self. color = color
        self. filled = filled 
        self. width = width 
        self. length = length
    def get_color(self): 
        return self. color
    def set_color(self): 
        return self. color 
    def is_filled(self): 
        return self. filled
    def set_filled(self, filled): 
        return self. filled
    def get_area():
        return (self.width * self.length)
#class Circle:
    def int (self, color, filled, radius): 
        self. color = color
        self. filled = filled 
        self. radius = radius
    def get_color(self): 
        return self. color
    def set_color(self): 
        return self. color
    def is_filled(self): 
        return self. filled
    def set_filled(self, filled): 
        return self. filled
    def get_area(self):
        return (math.pi * self. radius ** 2)
#----------------------------------------------------------------------------------------------------------
import math 
class Shape:
    def __init__(self, color='red', filled=False): 
        self. color = color
        self. filled = filled
    def get_color(self): 
        return self. color
    def set_color(self, color): 
        self. color = color
    def get_filled(self): 
        return self. filled
    def set_filled(self, filled): 
        self. filled = filled
class Rectangle(Shape):
    def __init__(self, length, breadth): 
        super().__init__()
        self. length = length 
        self. breadth = breadth
    def get_length(self): 
        return self. length
    def set_length(self, length):
        self. length = length
    def get_breadth(self): 
        return self. breadth
    def set_breadth(self, breadth): 
        self. breadth = breadth
    def get_area(self):
        return self. length * self. breadth
    def get_perimeter(self):
        return 2 * (self. length + self. breadth)
class Circle(Shape):
    def __init__(self, radius): 
        super().__init__() 
        self. radius = radius
    def get_radius(self): 
        return self. radius
    def set_radius(self, radius): 
        self. radius = radius
    def get_area(self):
        return math.pi * self. radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self. radius
r1 = Rectangle(13.5, 4.5)
print("Area of rectangle r1:", r1.get_area()) 
print("Perimeter of rectangle r1:", r1.get_perimeter()) 
print("Color of rectangle r1:", r1.get_color()) 
print("Is rectangle r1 filled ? ", r1.get_filled()) 
r1.set_filled(True)
print("Is rectangle r1 filled ? ", r1.get_filled()) 
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())
c1 = Circle(12)
#Roll No: Section:
print("\nArea of circle c1:", format(c1.get_area(), "0.2f")) 
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f")) 
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled ? ", c1.get_filled()) 
c1.set_filled(True)
print("Is circle c1 filled ? ", c1.get_filled()) 
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())        
#-------------------------------------------------------------------------------------------------------- 

class Classic_Umbrella:
    def __init__(self,material,style,prints,size,used_for):
        self.material=material
        self.style=style
        self.prints=prints
        self.size=size
        self.used_for=used_for
    def ForRain(self):
        return("This is the most common type of modern foldable umbrellas. Commonly made with {} to keep the rain off, these umbrellas are your everyday portable shelters from storms.Its style is {} and its printing is{} Its size is {}.This Umbrella is used for Both {} \n".format(self.material,self.style,self.prints,self.size,self.used_for))        
class Bubble_Umbrella:
    def __init__(self,fmaterial,fstyle,fprints,fsize,fused_for):
        self.fmaterial=fmaterial
        self.fstyle=fstyle
        self.fprints=fprints
        self.fsize=fsize
        self.fused_for=fused_for
    def ForSunprotection(self,colors):
        self.fcolors=colors
        return("This is the most commmon type of foldable umbrella.commonly made up of {} to Sunprotection and rainfalls.These are great for {} who love to peer out at the rain while keeping their faces dry.Its style is {} and its printing is{} Its size is {}.Its has diffrents colos {}".format(self.fmaterial,self.fused_for,self.fstyle,self.fprints,self.fsize,self.fcolors))        
       
class Automatic_Umbrella(Classic_Umbrella,Bubble_Umbrella):
    def __init__(self,material,style,prints,size,used_for,fmaterial,fstyle,fprints,fsize,fused_for):
        Classic_Umbrella.__init__(self,material,style,prints,size,used_for)
        Bubble_Umbrella.__init__(self,fmaterial,fstyle,fprints,fsize,fused_for)
    
AU=Automatic_Umbrella("metal of polyesther shafts with microfiber fabric canopys","Classic","Screenprinting","20 to 40 inches","Adults and kids","clear plastic","Kids","Bubble","Digital printing","20 to 40 inches")
print(AU.ForRain())
#AH=Automatic_Umbrella("clear plastic","Kids","Bubble","Digital printing","20 to 40 inches")
print(AU.ForSunprotection("[red,green,blue]"))



#------------------------------------------------------------------------------------------------------------------
class Classic_Umberalla:
    def __init__(self,material,style,prints,size,used_for):
        self.material=material
        self.style=style
        self.prints=prints
        self.size=size
        self.used_for=used_for
    def ForRain(self):
        return("This is the most common type of modern foldable umbrellas. Commonly made with {} to keep the rain off, these umbrellas are your everyday portable shelters from storms.Its style is {} and its printing is{} Its size is {}.This Umbrella is used for Both {} \n".format(self.material,self.style,self.prints,self.size,self.used_for))
    def WaterProof(self):
        return("This classic umbrella comes with a black waterproof case. Put the umbrella in the case to stop water leaking in your car, bag floor etc.\n")
    def Open_close(self):
        return("In this umberalla their is button to open and close \n")
class Bubble_Umbrella:
    def __init__(self,fmaterial,fstyle,fprints,fsize,fused_for):
        self.fmaterial=fmaterial
        self.fstyle=fstyle
        self.fprints=fprints
        self.fsize=fsize
        self.fused_for=fused_for
    def ForSunprotection(self,colors):
        self.fcolors=colors
        return("This is the most commmon type of foldable umbrella.commonly made up of {} to Sunprotection and rainfalls.These are great for {} who love to peer out at the rain while keeping their faces dry.Its style is {} and its printing is{} Its size is {}.Its has diffrents colos {} \n".format(self.fmaterial,self.fused_for,self.fstyle,self.fprints,self.fsize,self.fcolors))        
    def WaterProof(self):
        return("This Bubb;le umbrella not come in water proof.Because it mostly use to protectsunshineand its is made form kids ") 
    def Open_close(self):
        return(" It allows you to open the umbrella quickly using one hand. Push the button once to automatically extend the umbrella open, press again to instantly fold the Umbrella.\n")
    
CU=Classic_Umberalla("metal of polyesther shafts with microfiber fabric canopys","Classic","Screenprinting","20 to 40 inches","Adults and kids")        
BU=Bubble_Umbrella("clear plastic","Kids","Bubble","Digital printing","20 to 40 inches")
print(CU.ForRain())
print(CU.WaterProof())
print(CU.Open_close())
print(BU.ForSunprotection("[red,green,blue]"))
print(CU.WaterProof())
print(CU.Open_close())
#----------------------------------------------------------------------------------------------
class Library:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.lenddict={}
    def displaybook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
              
    def lendbook(self,username,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:username})
            print(f"Lender database  book has been updated. you can take the book now ")
        else:
            print(f"Book is already been taken by some one {self.lenddict[book]}")
    def addbook(self):
        self.booklist.append(book)
        print("Book has been added to the book list")
    def returnbook(self,book):
        self.lenddict.pop(book)
if __name__=='__main__':
    lib=Library(["Python","C++","C-sharp","Java","Javascript","R-language","Harrypotter","CLRS","Rish Daddy poor Daddy"],"Austrain library")

    while(True):
        print(f"Welcome to the {lib.name} library.Enter to choice to continue")
        print("1)  Display Book")
        print("2)  Lend a Book")
        print("3)  Add a Book")
        print("4)  Return a Book")
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("Please enter a Valid Option")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice ==1:
            lib.displaybook()
        elif user_choice ==2:
            book=input("Enter the book you want to lend")
            username=input("Enter your Name")
            lib.lendbook(username,book)
        elif user_choice ==3:
            book=input("Enter the book you want to add")
            lib.addbook(book)
        
        elif user_choice ==4:
            book=input("Enter the book you want to return")
            lib.returnbook(book)
            
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
#---------------------------------------------------------------------------------------------
class Bank:
    def __init__(self,bank_location,bank_Name,bank_code,bank_local_currency,bank_discount_currency):
        self.bank_location=bank_location
        self.bank_Name=bank_Name
        self.bank_code=bank_code
        self.bank_local_currency=bank_local_currency
        self.bank_discount_currency=bank_discount_currency
        
    def Bank_detailed(self):
        return(f"The name of the Bank is {self.bank_Name} near {self.bank_location}. Bank code is {self.bank_code} .Bank Local currency is {self.bank_local_currency} \n discount currency is {self.bank_discount_currency}")

class Account(Bank):
    def __init__(self,bank_location,bank_Name,bank_code,bank_local_currency,bank_discount_currency):
        Bank.__init__(self,bank_location,bank_Name,bank_code,bank_local_currency,bank_discount_currency)
class Banker(Account):
    def __init__(self,bank_location,bank_Name,bank_code,bank_local_currency,bank_discount_currency,Name):
        Account.__init__(self,bank_location,bank_Name,bank_code,bank_local_currency,bank_discount_currency)
        
        self.Name=Name
        
    def ManagerDetail(self):
        return(f"Hello Sir my name is {self.Name} \n  How can I help you sir? I deals All the customer those need loans if you can by a loan told me your account details")

    #print("How can I help you sir? I deals All the customer those need loans if you can by a loan told me your account details")

    def  verification(self,customer_detail,customer_Name,customerAccount_Number,x,loan):
        self.x=x
        self.customer_detail=customer_detail
        self.customer_Name=customer_Name
        self.customerAccount_Number=customerAccount_Number
        self.loan=loan
        if(self.x=="yes"):
            print(f"The User name is  {self.customer_Name}\n The User Account number is {self.customerAccount_Number}\n And Its Detail are {self.customer_detail} .\n After Checking your previous record Bank give A loan of Rs={self.loan}")
            
        else :
            print("sir Kindy open your accounr First then I would give a loan")
    
x=input("Do you have an account Sir please reply in yes/no ") 
customer_Name=input("Please tell me  your name Sir")
customerAccount_Number=input("Please tell me  your Account Number")
loan=input("How many loan you want to buy")
ba=Banker("Near Nazimabad","HBL Limited","#2768","pk","######","Bilal") 
print(ba.Bank_detailed())
print(ba.ManagerDetail())
print(ba.verification(["BankBalance of your account is Rs=340000"],customer_Name,customerAccount_Number,x,loan))        
   


    
      