#base class, parent class , common attribute + functionality class
#derived class, child class, uncommon attribute

class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.origin = origin
    def run(self):
        return f'margaya zindagi using phone tipa tipi' 

class Laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd
    
    def coding(self):
        return f'learning python and practicing'

class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
    
    def phone_call(self,number,text):
        return f'Sending SMS to {number} with {text}'
    
    def __repr__(self) -> str:
        return f'Phone: {self.brand} price: {self.price} , color: {self.color}, Origin: {self.origin}'

class Camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel
    
    def change_lense(self):
        return f'lance change koro'

#inheritance 

my_phone= Phone('iphone',120000,'silver','china',True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)