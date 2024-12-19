class Account:
    def __init__(self,balance:float,name:str):
        self.name = name
        self.__balance = balance   #private
    
    def set_balance(self,balance:float):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def show_acc(self):
        print("Name ",self.name)
    

class Loan:
    def __init__(self ,loan_balance:float):
        self.__loan_balance = loan_balance #private
    
    def set_loan_balance(self,loan_balance:float):
        self.__loan_balance = loan_balance
    
    def get_loan_balance(self):
        return self.__loan_balance
    

class PremiumAccount(Account,Loan):
    def __init__(self, balance:float, loan_balance:float, name:str):
        Account.__init__(self, balance, name)
        Loan.__init__(self,loan_balance)
    

    def get_total_balance(self):
        print(f"Get total balance : ",self.get_balance() + self.get_loan_balance())

        
obj:PremiumAccount=PremiumAccount(10.0, 500.5, "M:Huzaifa") 
obj.set_balance(100000.0)
obj.set_loan_balance(30000.0)
obj.show_acc()
print("Get loan balance",obj.get_loan_balance())
print("Get balance :",obj.get_balance())
obj.get_total_balance()
        








    