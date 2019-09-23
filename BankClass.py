class Account():
    '''
    Bank with deposit and withdra facility 
    
    '''
    
    def __init__(self,name,bal):
        self.name = name 
        self.bal = bal
    
    def depos(self,amt):
        
        self.bal = self.bal + amt
        
        return " The total available balance is = {}".format(self.bal)
    
    def withdraw(self,amt):
        
        if amt > self.bal :
            return " Insuffiecient Fund !!!"
        else:
            self.bal = self.bal - amt
            return " Amount withdrawn is {0} and available balance is {1}".format(amt,self.bal)
    
    def __str__(self):
        return f"Account Name = {self.name}  Account Balance = {self.bal}"
    