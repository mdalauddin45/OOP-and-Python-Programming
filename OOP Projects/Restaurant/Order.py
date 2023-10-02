from Menu import Menu
class Order:
    def __init__(self) -> None:
        self.items=[]
    
    def add_item(self,item,quantity=1):
        self.items.extend([item] * quantity)
    
    def remove_item(self,item_name):
        new_items=[]
        removed=False
        for item in self.items:
            if item.name != item_name:
                new_items.append(item)
            else:
                removed=True
        self.items = new_items
        if removed:
            print('Successfully removed item ', item_name)
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    def display_order(self):
        print("Order")
        for item in self.items:
            print(item)
    
helo=Order()
alo = Menu()
print(alo)
helo.add_item("jabab")
helo.remove_item('kabab')
helo.add_item("nabab")
# helo.display_order()