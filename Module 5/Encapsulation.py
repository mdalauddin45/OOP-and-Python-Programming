# encapsulation --> hide details
# access modifire --> public ,private, protected
class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        #public attribute
        self.holder_name=holder_name
        #__ is private attribute
        self.__balance=initial_deposit
        #_ protected attribute
        self._branch = 'rowshonhat branch'
    
    def deposit(self,amout):
        self.__balance +=amout
        
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance = self.__balance-amount
            return f'{self.__balance}'
        else:
            return f'sala fokira '

rafsan = Bank('chootoo bro',10000)
print(rafsan.holder_name)
rafsan.holder_name='boro vhai'
# rafsan.balance=0
# print(rafsan.__balance)
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan.holder_name)
# print(rafsan._branch)

print(rafsan.withdraw(400))
print(rafsan._Bank__balance)
print(dir(rafsan))