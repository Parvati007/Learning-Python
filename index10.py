#OOPS IN PYTHON

#ABSTRACTION:- hiding the implementation details of class and only showing the essential features to the user.

#ENCAPSULATION:- wrapping data and functions into a single unit(objects)

#--------------------------------------------------------------------------------
#create a Account class with 2 attributes balance and accoun_tno
#then create methods for debit,credit and printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount 
        print("RS. ",amount,"was debited")  
        print('total balance is : ',self.balance) 

    def credit(self,amount):
        self.balance+=amount 
        print("RS. ",amount,"was credited")  
        print('total balance is : ',self.balance)
    
    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)    