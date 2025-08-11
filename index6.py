#FUNCTIONS:-
#block of statement that perform a specific task

def cal_sum(a,b):    #function definition...parameters
    return a+b

output =cal_sum(1,2)       #function call...arguments
#print(output)

#-------------------------------------------------------
def print_hello():
    print("hello world")

#print_hello()           #hello world
out=print_hello()
#print(out)               #None

#------------------------------------------------------
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

#calc_avg(1,2,3)         #2.0

#---------------------------------------------------
#1. built-in functions :- print(),type(),range()
#2. user defined function

#---------------------------------------------------
#default parameters:- assigning a default value to parameter which is used when no arguments is passed

def cal_prod(a=1,b=1):
    print(a*b)
    return a*b
cal_prod()                         #1

# def cal_prod(a=1,b):
#     print(a*b)
#     return a*b
# cal_prod(1)                       #error will occur

def cal_prod(a,b=2):
    print(a*b)
    return a*b
cal_prod(1)                        #2

#----------------------------------------------------------------------