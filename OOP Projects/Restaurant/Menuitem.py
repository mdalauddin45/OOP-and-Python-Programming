class MenuItem:
    def __init__(self,name,price,description) -> None:
        self.name=name
        self.price=price
        self.description=description
    def __str__(self) -> str:
        return f'Name: {self.name}, Description {self.description} , Price:  ${self.price}'
    
# alo = MenuItem('kabab',12,'kabab may haddi')
# print(alo)
