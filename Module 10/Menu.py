class Food:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15 

class Burger(Food):
    def __init__(self, name, price,meat,ingradients) -> None:
        self.meat = meat
        self.ingradients = ingradients
        super().__init__(name, price)

class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        self.size =size
        self.toppings=toppings
        super().__init__(name, price)

class Drinks(Food):
    def __init__(self, name, price,isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

#composition
class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = [] 
        
    def add_manu_item(self,item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)
        else:
            print(f'not found')
    
    # def remove_item(self,item):
    #     if item == ''
    
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
            
    def show_menu(self):
        for pizza in self.pizzas:
            print(f'Name: {pizza.name} Price: {pizza.price}')
        for burder in self.burgers:
            print(f'Name: {burder.name} Price: {burder.price}')
        for drink in self.drinks:
            print(f'Name: {drink.name} Price: {drink.price}')