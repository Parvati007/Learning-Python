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