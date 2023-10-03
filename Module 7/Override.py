class Person:
    def __init__(self,name,age,hight,weight) -> None:
        self.name=name
        self.age=age
        self.hight=hight
        self.weight=weight
    
    def eat(self):
        print('vat mangso polau kormaa')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, hight, weight,team) -> None:
        self.team=team
        super().__init__(name, age, hight, weight)
        
    def eat(self):
        print('Vagitable kamu')
    
    def exercise(self):
        print('gym a poisa diya hudai gham jorai')
        
    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.weight * other.weight
    def __len__(self):
        return self.hight
    def __gt__(self,other):
        return self.age>other.age

sakib=Cricketer('sakib',30,5,60,'bd')
mushi = Cricketer('mushi',36,65,78, "BD")

# sakib.eat()
# sakib.exercise()
# print(sakib)

#plus sign overload
# print(45+65)
# print( 'sakib'+'rakib')
# print([12,454,65,8]+[34,67,32,7,41,90])
print(sakib+mushi)
print(sakib*mushi)
print(len(sakib))
print(sakib>mushi)