#Ena Poribohon

class Company:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisor=[]

class Drivers:
    def __init__(self,name,licence,age) -> None:
        self.name=name
        self.licence=licence
        self.age=age
    def __repr__(self) -> str:
        print(f'{self.name} {self.age} {self.licence}')
        return 'Driver done'

class Counter:
    def __init__(self,address,fromto) -> None:
        self.address=address
        self.fromto=fromto
    def purchase_a_ticket(self,start,destination):
        pass

class Passenger:
    pass
class Supervisor:
    pass

red_mia=Drivers('red',234,34)
print(red_mia)
