#OOPS IN PYHTON

#del keyword- used to delete object properties or object itself
#ex: del s1.name
#ex: del s1

#------------------------------------------------------------------
#PRIVATE(like) attributes and methods
#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
#__name ....way to make a private attribute

class Person:
    __name="anonymous"
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()    

p1=Person()
print(p1.welcome())    #hello person will printed no error
print(p1.__hello())    #error will occur because it is private

#---------------------------------------------------------------------
#INHERITANCE
#when one class (child/drived) derives the properties and methods of another(parent/base)class
#(parent/base class)<----------------(child/derived class)

class Car:
    color="black"