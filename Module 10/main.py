from Menu import Pizza, Burger, Menu, Drinks

def main():
    menu = Menu()
    pizza_1 = Pizza("Shutki pizza",600,"large",['shutki','onion'])
    pizza_2 = Pizza("Alur Vorta pizza",400,"large",['Potato','onion','oil'])
    menu.add_manu_item('pizza',pizza_1)
    pizza_3 = Pizza("Dal pizza",500,"large",['dal','oil'])
    menu.add_manu_item('pizza',pizza_2)
    menu.add_manu_item('pizza',pizza_3)
    
    
    burger_1 = Burger('naga burger',1000,'chicken',['bread','chili'])
    burger_2 = Burger('Beef burger',1000,'Beed',['goru','haddi'])
    menu.add_manu_item('burger',burger_1)
    menu.add_manu_item('burger',burger_2)

    coke = Drinks('coke',50,True)
    pepsi = Drinks('pepsi',30,True)
    coffee = Drinks('coffe',300,False)
    menu.add_manu_item('drinks',coke)
    menu.add_manu_item('drinks',pepsi)
    menu.add_manu_item('drinks',coffee)
    
    # show Menu
    menu.show_menu()
# call the  main() 
if __name__ == '__main__':
    main()