def call(self):
    print('calling someone i dont know')
    return 'call done'
class Phone:
    price = 190000
    color = 'black'
    brand= 'iphone'
    features=['camera','speaker','hammer']
    def call(self):
        print('calling one person')
    
    def send_sms(self,phone,sms):
        text = f'sending SMS to : {phone} and message : {sms}'
        return text
        
my_phone= Phone()
print(my_phone) #print addres of phone
print(my_phone.brand)
print(my_phone.price)
print(my_phone.color)
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(323847,'i Miss you')
print(result)