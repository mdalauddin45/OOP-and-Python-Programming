class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
    
    def diposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'after {amount} tk deposit your balance is {self.balance}')
        else:
            print('minimum 1 tk deposit kora lagby')
            
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print(f'sala fokir, you can not withdrow below {self.min_withdraw}')
        elif amount>self.max_withdraw:
            print(f'tumi fokir hya jaba bro if you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance-=amount
            print( f'{amount} Tk withdrow successfull!')
            print( f'Your balace after withdrow {self.get_balance()}')
            # print( f'Your balace after withdrow {self.balance}')

brac = Bank(15000)
# brac.withdraw(1000)
brac.diposit(1)