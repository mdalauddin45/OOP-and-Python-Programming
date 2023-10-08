from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email= email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address,money) -> None:
        self.wallet = money
        self.__order= None
        super().__init__(name, phone, email, address)
        
            
    @property #todo
    def order(self):
        return self.__order
    
    @order.setter #todo
    def order(self,order):
        self.__order = order
    
    def place_order(self,order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')
    
    def eat_food(self,order):
        print(f'{self.name} item food {order.items}')
    
    def pay_for_order(self,amount):
        #todo submit the money to the manager
        pass

    def give_tips(self,tips_amount):
        pass
    
    def write_rivew(self,stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address ,salary,starting_date,department) -> None:
        super().__init__(name, phone, email, address)
        self.salary=salary
        self.starting_date = starting_date
        self.department = department
        
class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_item=cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earnig=0
        super().__init__(name, phone, email, address, salary, starting_date, department)
    
    def take_order(self,order):
        pass
    
    def trasfer_order(self,order):
        pass
    
    def serve_food(self,order):
        pass
    
    def recive_tips(self,amount):
        self.tips_earnig+=amount
        
class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)