class Shop:
    shopping_mall= 'jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []  #cart is an instance attribute
    def add_to_cart(self,item):
        self.cart.append(item)

mehzabeen = Shop('meh jabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('cap')
print(nisho.cart)

apurbo = Shop('apurbo')
apurbo.add_to_cart('ciruni')
apurbo.add_to_cart('car')
print(apurbo.cart )