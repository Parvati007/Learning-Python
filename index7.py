#RECURSION
#when a function call itself repeatedly

def show(n):
    if(n==0):    #base case
        return
    print(n)
    show(n-1)
show(5)                           # 5 4 3 2 1


def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(6))                 #720

#--------------------------------------------------------------------------
#Write a recursive function to calculate the sum of first n natural numbers
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)                    #15

#---------------------------------------------------------------------------
#write a recursive function to print all elements in a list 
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print( list[idx])
    print_list(list,idx+1)

fruits=["apple","litchi","banana","mango"]
print_list(fruits)    