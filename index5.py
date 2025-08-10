#LOOPS
#loops are used to reoeat instructions
#there are two types of :- 
#1. WHILE LOOP
#2. FOR LOOP

# i=1
# while i<=5 :
#     print("hello")
#     i+=1

# print("end of loop")    

#print numbers from 1 to 100
# i=1
# while i<=100 :
#     print(i)
#     i+=1

# print("end of loop")   

#print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# print("end of loop")  


# Print the multiplication table of number n
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1
# print("End of loop")
 

#print the elements of following list using loop
# nums=[1,4,8,16,25,36,49,64,81,100]
# i=0
# while i< len(nums) :
#     print(nums[i])
#     i+=1

# print("end of loop") 

#search for a number x in this tuple using the loop
# tup=(1,3,4,6,7,89,76,45)
# x=76
# i=0
# while i< len(tup) :
#     if(tup[i]==x):
#         print("FOUND")
#     else:
#         print("finding...")    
#     i+=1
# print("end of loop")        

#BREAK :- used to terminate the lop when executed
#CONTINUE :- terminates execution in the current iteration and continues execution of the loop with the next iteration

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("end of loop") 

#printing odd numbers only
# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("end of loop")     #output....1,3,5,7,9

#----------------------------------------------------------------------
#FOR LOOP
#used for sequential traversal for traversing list,string,tuples.

#for loop

# list=[1,2,3,4]
# for el in list:
#     print(el)

# veggies=["potato","tomato"]
# for el in veggies:
#     print(el)

# tup=(1,2,3,4,5,6,7,8)
# for el in tup:
#     print(el)

# str="parvati"
# for el in str:
#     print(el)

# for_with_else=[1,2,3,4,5,6]
# for el in for_with_else :
#     print(el)
# else:
#     print('END')   

#search for a number x in tuple using for loop
# num=(1,2,3,4,59,67,89)
# x=67
# i=0
# for el in num:
#     if(num[i]==x):
#         print("found at index : ",i)
#         break
#     i+=1

#--------------------------------------------------------
#RANGE() :- a function returns a sequence of numbers
#staring from 0 by default
#increment by 1 by default
#stops before a specified number

#range(start?,stop,step?)

# for el in range(5):           #0,1,2,3,4
#     print(el)

# for el in range(1,5):         #1,2,3,4
#     print(el)

# for el in range(1,5,2):       #1,3
#     print(el) 

#print number from 1 to 100 using range
# for i in range(1,101):
#     print(i) 

#print number from 100 to 1 using range
# for i in range(100,0,-1):
#     print(i)

#print the multiplication table of number n
#n=int(input("enter a number : "))
# for i in range(1,11):
#     print(n*i)

#-----------------------------------------------
#pass statement:- it is a null statement that does nothing. it is used as placeholder for future code
# for i in range(10):
#     pass

#find the sum of first n natural numbers using while
n=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum is : ",sum)

#find factorial of first n numbers usinf for
n=5
fact =1
for i in range(1,n+1):
    fact*=i
print("factorial : ", fact)    
                                
 
     

