class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    
    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    
    def remove_item(self,item):
        removed=False
        for product in self.cart:
            if product['item']==item:
                self.cart.remove(product)
                print(f'{item} removed form the cart')
                removed=True
                break
        if not removed:
            print({f'{item} no found in the cart'})
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            print(item)
            total+=item['price']*item['quantity']
        print(f'total price {total}')
        if amount<total:
            print(f'pleace provide {total-amount} more')
        else:
            print(f'tmi perot paba {amount-total}')
        
alo=Shopping('ala uddin')
alo.add_to_cart('rice',75,20)
alo.add_to_cart('alu',12,1)
alo.add_to_cart('dim',20,1)
# print(alo.cart)
alo.remove_item('dim')
alo.checkout(600)