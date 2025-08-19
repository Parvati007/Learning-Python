#OOPS (object oriented programming) IN PYTHON
#to map with real world scenarios we started using objects in code.this is called oop

#----------------------------------------------------------------------------------
#CLASS AND OBJECTS
#class is blueprint for creating objects
#object is instance of class

#example :-
# class Student:
#     name="parvati"

# s1=Student()
# print(s1.name)

# class Car:
#     brand="BMW"
#     color="green"

# car1=Car()
# print(car1.brand)
# print(car1.color)   
#------------------------------------------------------

#CONSTRUCTOR  __init__ function
# all class have function called __init__ which is always executed when the object is being initiated
#
#example:-
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student data..")   

# s1=Student("parvati",97)
# print(s1.name,s1.marks)

# s2=Student("aditi singh",100)
# print(s2.name,s2.marks)

#constructor are of two types
#1. default
#2. parameterized

#-------------------------------------------------------------------------
#CLASS ATTRIBUTES AND OBJECT ATTRIBUTES
#note:- obj attr >>> class attr
#example..........cls attr---->college name
#example..........obj attr----> student name 
#-------------------------------------------------------------------------
#METHODS
# methods are function that belongs to objects

class Student:
    college_name="ABC"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks

s1=Student("paru",97)
s1.welcome()                         #welcome student paru
print(s1.get_marks())                #97

