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
i=100
while i>=1:
    print(i)
    i-=1

print("end of loop")  


# Print the multiplication table of number n
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
print("End of loop")
 

#print the elements of following list using loop
nums=[1,4,8,16,25,36,49,64,81,100]
i=0
while i< len(nums) :
    print(nums[i])
    i+=1

print("end of loop") 

#search for a number x in this tuple using the loop
tup=(1,3,4,6,7,89,76,45)
x=76
i=0
while i< len(tup) :
    if(tup[i]==x):
        print("FOUND")
    else:
        print("finding...")    
    i+=1
print("end of loop")        

#BREAK :- used to terminate the lop when executed
#CONTINUE :- terminates execution in the current iteration and continues execution of the loop with the next iteration

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop") 

#printing odd numbers only
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
print("end of loop")     #output....1,3,5,7,9
