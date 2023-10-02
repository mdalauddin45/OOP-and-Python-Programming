from abc import ABC, abstractmethod
#abstrac base class
class Animal(ABC):
    @abstractmethod #inforce all derive class to have a eat method
    def eat(self):
        print('hey nana, eatting banana')
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name=name
        self.category='Monkey'
        super().__init__()
    def eat(self):
        print('hey na nana, I am eatting banana')
        
    def move(self):
        print('Hanging on the branchers')
        
layka = Monkey('Lucky')
layka.eat()