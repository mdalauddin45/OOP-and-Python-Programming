class Phone:
    manufactured = 'china'
    #one kind of constructor
    def __init__(self,owner,brand,price):
        self.owner= owner
        self.brand = brand
        self.price=price
        
    def send_sms(self,phone,sms):
        text=f'sending to: {phone} {sms}'
        print(text)

my_phone=Phone('alauddin','iphone',190000)
print(my_phone.brand,my_phone.owner,my_phone.price)

her_phone=Phone('it s haram bro','oppo','1100')
print(her_phone.owner,her_phone.price,her_phone.brand)

my_phone.send_sms(my_phone.brand,her_phone.owner)
her_phone.send_sms(her_phone.brand,her_phone.price)

dad_phone=Phone('baba',' Nokia',47312)
print(dad_phone.owner,dad_phone.price,dad_phone.brand)
