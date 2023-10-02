# Create a Product class and a Shop class.
# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
# Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.

class Product:
    def __init__(self,id,name,price,stock) -> None:
        self.id=id
        self.name=name
        self.price=price
        self.stock = stock
    def __repr__(self) -> str:
        return f'Product ID: {self.id}, Name: {self.name}, Price: ${self.price}, Strock: {self.stock}'

class Shop:
    def __init__(self) -> None:
        self.products=[]
        
    def add_product(self,product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f'Product {product.name} added to the shop')
        else:
            print("Invalid Product. Please provide a valid product")
    def buy_product(self,id):
        for product in self.products:
            if product.id==id:
                if product.stock>0:
                    product.stock-=1
                    print(f"Congratulation! You have Sucessfully Purchesd {product.name}.")
                    return
                else:
                    print(f"Sorry, {product.name} is out of stock")
                    return 
        print("Product not found in the shop")
    def __repr__(self):
        for product in self.products:
            print(product)
        return f'Thanks for visiting my shop'

shop =Shop()
product1=Product(1,"Laptop",999.99,5)
product2=Product(2,"Smartphone",599.99,2)
product3=Product(3,"tv",899.99,4)
product4=Product(4,"fridge",499.99,8)
product5=Product(5,"pc",799.99,3)

shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product2)
shop.add_product(product3)
shop.add_product(product4)
shop.add_product(product5)

# shop.buy_product(2)
# shop.buy_product(2)
# shop.buy_product(2)
print(shop)
        
    