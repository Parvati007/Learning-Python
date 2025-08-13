#INTRODUCTION OF PYTHON

#Writing first program in python
#print("Hello World!!")
#print("My name is PARVATI.", "My age is 21.")
#print(25+36)
#---------------------------------------------------
#Variables
# name="PARVATI"
# age=21
# price=25.99
# old=False
# z=None
# print(name,age,price)
#----------------------------------------------------
#Data Types
# print(type(name))  #str
# print(type(age))   #int
# print(type(price)) #float
# print(type(old))   #bool
# print(type(a))     #NoneType
#----------------------------------------------------
#print sum of two numbers
# a=2
# b=5
# sum=a+b
# print(sum)

#division 
# A,B=1,2
# C=A/B
# print(C)   #0.5

# #integer division
# a,b=1,2
# c=a//b
# print(c)   #0

# x,y=1.5,3
# z=x//y
# print(z)   #0.0
#---------------------------------------------------------------------
#Comments in python
#1. single line.............#content
#2. multi line............."""content"""
#---------------------------------------------------------------------
#Expression Execution 
#1. string and numeric values can operates together with * (repeat).
#2. string and string can operate with + (concatenation).
#3. numeric value can operate with all arithmetic operator.
#4. arithmetic expression with integer and float will result in float.
#5. result of division operator with two integer will be float.
#6. Integer division(//) with float and int will give int but displayed as float.
#7. Integer divison with int and int result in int also.
#8. remainder is negative when the denominator is negative.
#---------------------------------------------------------------------
#Taking input from the user in python
# name=input("name is : ")
# age=int(input("age is : "))
# price=float(input("price is : "))
# print("my name is ",name,".I am",age,"years old.")
#----------------------------------------------------------------------
#Conditional statements

#traffic lights code
# light=input("light is : ")
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")   

#grades of students
# marks=int(input("marks is : "))
# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<90):
#     print("B")
# elif(marks>=70 and marks<80):
#     print("C")
# else:
#     print("D")  

#-----------------------------------------------
#Ternary operator
# food = input("food is : ")
# eat ="yes" if food=="cake" else "no"
# print("Eat?", eat)


# drink = input("drink is : ")
# print("colddrink") if drink=="fanta"or drink=="coca cola" else print("no drinks")

#Clever-If
#var = (false , true) [condition]
# age= int(input("age is : "))
# vote = ("yes","no") [age<18]
# print("vote?", vote)

# sal=float(input("salary is : "))
# tax=sal*(0.1,0.2) [sal>50000]
# print("tax is : " ,tax)
#---------------------------------------------------
#Arithmetic operators
# a=5
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
#---------------------------------------------------
#Comparison operator (boolean)
# a=10
# b=20
# print(a==b) #False
# print(a!=b) #True
# print(a>b)  #False
# print(a<b)  #True
# print(a>=b) #False
# print(a<=b) #True
#---------------------------------------------------
#Assignment operator
# num = 10
# num += 10
# print(num)
# num -= 10
# print(num)
# num *= 10
# print(num)
# num /= 10
# print(num)
# num %= 10
# print(num)
# num **= 10
# print(num)

#Logical operator (boolean)
# a=50
# b=20
# print(not False)  #True
# print(not (a>b))  #False

# val1=True
# val2=True

# print("AND operation : ", val1 and val2)
# print("OR operation : ",val1 or val2)
#------------------------------------------------
#Type conversion.....automatically
# a=10
# b=100.0
# print(a+b)  #110.0

#Type casting.......manually
# a=int("2")
# b=10
# print(a+b)          #12

# a=int("2")
# b=15.7
# print(a+b)           #17.7



