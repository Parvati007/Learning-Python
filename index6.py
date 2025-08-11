#FUNCTIONS:-
#block of statement that perform a specific task

# def cal_sum(a,b):    #function definition...parameters
#     return a+b

# output =cal_sum(1,2)       #function call...arguments
#print(output)

#-------------------------------------------------------
# def print_hello():
#     print("hello world")

#print_hello()           #hello world
#out=print_hello()
#print(out)               #None

#------------------------------------------------------
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

#calc_avg(1,2,3)         #2.0

#---------------------------------------------------
#1. built-in functions :- print(),type(),range()
#2. user defined function

#---------------------------------------------------
#default parameters:- assigning a default value to parameter which is used when no arguments is passed

# def cal_prod(a=1,b=1):
#     print(a*b)
#     return a*b
# cal_prod()                         #1

# def cal_prod(a=1,b):
#     print(a*b)
#     return a*b
# cal_prod(1)                       #error will occur

# def cal_prod(a,b=2):
#     print(a*b)
#     return a*b
# cal_prod(1)                        #2

#----------------------------------------------------------------------
#WAF to print the length of list ...list is the parameter
# cities=["noida","jaipur","udaipur","delhi"]

# def print_len(list):
#     print(len(list))

#print_len(cities)    #4   
#----------------------------------------------------------------------
#WAF to print the elements of a list in single line..list is parameter
# cities=["noida","jaipur","udaipur","delhi"]

# def print_list(list):
#     for item in list:
#         print(item,end=" ")
#print_list(cities)        #noida jaipur udaipur delhi

#-----------------------------------------------------------------------
#WAF to find the factorial of n ....n is parameter
def print_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)        
print_fact(5)    

#------------------------------------------------------------------------
#WAF to convert usd to inr...1 usd = 83 inr
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD = ",inr_val,"INR")

converter(100) 

#-----------------------------------------------------------------------
#WAF to echeck even and odd number

n= int(input("Enter a number :"))

def num_check(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

num_check(n)


