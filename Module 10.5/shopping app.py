class Sufi_Shopping_mall:
    seller_list=[]
    custormer_list=[]
    def entry_selle(self,seller):
        self.seller_list.append(seller)
        
    def entry_customer(self,customer):
        self.custormer_list.append(customer)
        
class User:
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password

class Product:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock

class Seller(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.products = []
    
    def publish_product(self,name,price,stock):
        product = Product(name,price,stock)
        self.products.append(product)
        print(f"Product {name} published successfully.")
    
class Customer(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.cart=[]
        
    def display_product(self,sellers):
        for seller in sellers:
            for product in seller.products:
                if product.stock>0:
                    print(f"Product: {product.name}, Price: ${product.price}, Stock: {product.stock}, Seller: {seller.email}")
                
    
    def place_order(self,product,quantity):
        if product.stock>=quantity:
            product.stock-=quantity
            self.cart.append((product,quantity))
            print(f"Added {quantity} {product.name}(s) to your cart.")
        else:
            print(f"Added {quantity} {product.name}(s) to your cart.")
    
    # def checkout(self):

shop = Sufi_Shopping_mall()
customer1 = Customer("customer1@email.com", "password1")
seller1 = Seller("seller1@email.com", "password2")
seller2 = Seller("seller2@email.com", "password3")

seller1.publish_product("Product A", 50, 10)
seller2.publish_product("Product B", 30, 5)

customer1.display_product([seller1, seller2])
        