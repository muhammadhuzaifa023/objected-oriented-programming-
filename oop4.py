# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:55:11 2020

@author: HASSAN ENTERPRISES
"""


#---------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------
class HUAWEI_Mobile:
    def Screen_size(self):
        return("The screen_size of HUWAEI_Y9 is 6.5inches")
    def  Microprocessor(self):
       return("The processor used in HUWAEI_Y9 is 2.2GHz octa-core")
    def size(self):    
       return("The size of Mobile is ")
    def Display(self):
       return("The display type of HUWAEI_Y9 is IPS LCD")
class  samsung_Mobile:
    def Screen_size(self):
        return("The screen_size of Samsung Note 10 is 6.3 inches")
    def  Microprocessor(self):
        return("The microprocessor used in Samsung Note 10 Snapdragon 855")
    def size(self):
        return("The size of samsung Note 10 is 151 x 71.8 x 7.9 mm")
    def Display(self):
        return("The display type of Samsung Note 10 is Dynamic AMOLED")
class Infinix_Mobile:
    def Screen_size(self):
        return("The screen size of Infinix_Hot 8 is 6.52 inches")
    def Microprocessor(self):
        return("The processor used in Infinix_Hot is Quad-core 2.0 GHz Cortex-A53")
    def size(self):
        return("The screen Size of Infinix_Hot 8 165 x 76.3 x 8.7 mm ")
    def Display(self):
        return("The display typeof infinix Hot 8 is IPS LCD capacitive touchscreen ")
HUA=HUAWEI_Mobile()
SAM=samsung_Mobile()
INF=Infinix_Mobile()
for Mobile in (HUA,SAM,INF):
    print(Mobile.Screen_size())
    print(Mobile.Microprocessor())
    print(Mobile.size())
    print(Mobile.Display()+"\n")