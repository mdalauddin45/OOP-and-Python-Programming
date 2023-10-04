#read only--> you can not set the value , 
# getter --> get a value of a property , Most of the time, you will get the value of a private attribute
# setter -->  get a value of a property , Most of the time, you will get the value of a private Property
class User:
    def __init__(self,name,age,money) -> None:
        self.name=name
        self._age=age
        self.__money=money
    
    #getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    #getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value<0:
            print('salary can not be negative')
        self.__money+=value
        
samsu = User('kopa', 21,12000)
print(samsu.salary)
print(samsu.age)
samsu.salary=4500
print(samsu.salary)