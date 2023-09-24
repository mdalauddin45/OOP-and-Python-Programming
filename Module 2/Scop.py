balance = 3000
dream_phone = None 
def buy_things(item,price):
    global balance
    global dream_phone
    balance=balance-price
    dream_phone= 'iphone'
    print(f'balance after buying {item}',balance)
    
buy_things('sunglass',1000)
print(f'Dream phone: {dream_phone}')