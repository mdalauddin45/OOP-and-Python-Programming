#poly --> many(multiple)
# morph --> shape

class Animal:
    def __init__(self,name) -> None:
        self.name=name
        
    def make_sound(self):
        print('animal making some sound')
        
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Meow meow')
        
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Gheu gheu')
        
        
class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Yeah hu Yeah hy')
        
        
dom = Cat('Real dom')
dom.make_sound()
# print(dom) 

she= Dog('Sha')
she.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

animal = [dom, she, mess,less]

for ani in animal:
    ani.make_sound()
