class Account():
    '''
    Bank with deposit and withdra facility  
    '''
    
    def __init__(self, name, bal):
        '''
        default init function or constructor
        '''
        self.name = name 
        self.bal = bal
    
    def depos(self, amt):
        '''
        Adds the amount to the balance 
        '''
        self.bal = self.bal + amt
        return " The total available balance is = {}".format(self.bal)
    
    def withdraw(self, amt):
        '''
        Deducts the bal as given amount 
        '''
        if amt > self.bal:
            return " Insuffiecient Fund !!!"
        self.bal = self.bal - amt
        return " Amount withdrawn is {0} and available balance is {1}".format(amt, self.bal)
    
    def __str__(self):
        '''
        default string function 
        '''
        return f"Account Name = {self.name}  Account Balance = {self.bal}"
    