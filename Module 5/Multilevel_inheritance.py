class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def __repr__(self) -> str:
        return f'{self.name} {self.price}'        
    def move(self):
        pass
class Bus(Vehicle):
    def __init__(self,name,price,seat) -> None:
        self.seat=seat
        super().__init__(name,price)
    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self,name,price,weight):
        self.weight=weight
        super().__init__(name,price)

class PickupTrack(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class ACBUS(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
        
green_line = ACBUS('Greeen',500000,23,34)
print(green_line)