class Shopping:
    cart=[] #class Attribute #Static Attribute
    origin = 'china'
    def __init__(self,name,location) -> None:
        self.name='Jamu na City' #instance attribute
        self.location = 'jem er maj khane'
    
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining : {remaining}')
    
    @staticmethod
    def multiply(a,b):
        print(a*b)
    
    @classmethod
    def hudai_dekhi(self,item):
        print('Hudai dekhi kintu kinmu na just ac er hawa khaite aschi',item)

basundara = Shopping('basu en dhara', 'not popular location')
basundara.purchase('lungi',500,1000)   

# Shopping.purchase("he",2,3)
basundara.hudai_dekhi('Lungi')
Shopping.hudai_dekhi('lungi')


basundara.multiply(45,6) 
Shopping.multiply(3,4) #static mathode