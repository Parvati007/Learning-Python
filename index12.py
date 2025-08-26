#OOPS IN PYTHON

#POLYMORPHISM---->many forms

#Operator Overloading:- when the same operator is allowed to have diff meaning according to the content
#print(1+2).............................addition....3
#print("apna"+"college")...............concatenate....apnacollege
#print([1,2,3]+[4,5,6]).................merge.......[1,2,3,4,5,6]
#implicit overloading h python ko pta h phele se above all..

#---------------------------------------------------------------------------
#Operator and Dunder function
#a+b...addition....   a.__add__(b)
#a-b...subtraction....   a.__sub__(b)
#a*b...multiplication....   a.__mul__(b)
#a/b...division....   a.__trudiv__(b)
#a%b...modulous....   a.__mod__(b)

#--------------------------------------------------------------------------

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showNumber(self):
#         print(self.real,"i + ",self.img,"j")
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)  
# num1=Complex(1,3)
# num1.showNumber()             #1i+3j
# num2=Complex(4,6)      
# num2.showNumber()             #4i+6j
# num3=num1+num2
# num3.showNumber()             #5i+9j 

#----------------------------------------------------------------------
#PRACTICE QUESTIONS

#1. define a circle class to create a circle with radius r using the constructor.
#define an area() method of class which calculates the area of the circle.
#define a perimeter() method of the class which allows you to calculate the perimeter of circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
c1=Circle(21)
print(c1.area())         #1386.0
print(c1.perimeter())    #132.0

#-------------------------------------------------------------------------------------------

        
