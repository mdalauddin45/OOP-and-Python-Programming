class Laptop:
    def __init__(self,brand,price,color,memory) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.memory=memory
    def run(self):
        return f'running laptop {self.brand}'
    
    def coding(self):
        return f'learning python and practicing'

class Phone:
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim
    
    def run(self):
        return f'margaya zindagi using phone tipa tipi' 
    def phone_call(self,number,text):
        return f'Sending SMS to {number} with {text}'

class Camera:
    def __init__(self,brand,price,color,pixel) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.pixel=pixel
    
    def run(self):
        return f'camera cholaw'
    
    def change_lense(self):
        return f'lance change koro'