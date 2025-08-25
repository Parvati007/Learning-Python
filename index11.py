#OOPS IN PYHTON

#del keyword- used to delete object properties or object itself
#ex: del s1.name
#ex: del s1

#------------------------------------------------------------------
#PRIVATE(like) attributes and methods
#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
#__name ....way to make a private attribute

# class Person:
#     __name="anonymous"
#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()    

# p1=Person()
# print(p1.welcome())    #hello person will printed no error
# print(p1.__hello())    #error will occur because it is private

#---------------------------------------------------------------------
#INHERITANCE
#when one class (child/drived) derives the properties and methods of another(parent/base)class
#(parent/base class)<----------------(child/derived class)

# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started...")
#     @staticmethod
#     def stop():
#         print("car stopped...")
# class ToyotaCar(Car):                   #single inheritance
#     def __init__(self,name):
#         self.name=name

# car1= ToyotaCar("fortuner")
# car2= ToyotaCar("prius")

# print(car1.color)                    #black
# print(car1.start())                  #car started...
#-----------------------------------------------------------
#Types of Inheritance
#1. single inheritance         base<---derived
#2. multi-level inheritance    base<---derived<----derived
#3. multiple inheritance       base1--->derived<----base2

#----------------------------------------------------------
#example of multi-level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print('car started...')
#     @staticmethod
#     def stop():
#         print('car stopped..') 
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type 

# Car1=Fortuner("diesel")
# print(Car1.start())                    #car started...no error
#------------------------------------------------------------------
#MULTIPLE Inheritance Example

# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class C"
# c1=C()
# print(c1.varC)#welcome to class C
# print(c1.varB)#welcome to class B
# print(c1.varA)#welcome to class A           

#----------------------------------------------------------
#Super method:-is used to access method of the parent class

# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car started...")
# class ToyotaCar(Car):
#     def __init__(self,name,type): 
#         super().__init__(type)          #car class is called
#         self.name=name 
#         super().start()                #car class is called
# car1=ToyotaCar("prius","electric")
# print(car1.type)

#-------------------------------------------------------------------
#CLASS METHOD
#a class method is based to the class and receives the class as an implicit first argument

#note:-static method can't access or modify class state and generally for utility

#types of method:
#1.static method
#2.class method(cls)
#3.instance method(self)

#ex:-
# class Person:
#     name="anonymous"
#     #def changeName(obj,name):
#     #    self.__class__.name="Rahul"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name
# p1=Person()
# print(Person.name)                  #anonymous
# p1.changeName("Rahul Kumar")
# print(p1.name)                      #Rahul Kumar                
# print(Person.name)                  #Rahul Kumar  


#---------------------------------------------------------------------
#PROPERTY
#we use @property decorator on any method in the class to use the method as a property
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property                      #attribute h usko bs method way me type kr rahe
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+" %"
stu1=Student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage) 





        