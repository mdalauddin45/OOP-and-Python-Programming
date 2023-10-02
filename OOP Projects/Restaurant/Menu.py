from Menuitem import MenuItem
class Menu:
    def __init__(self) -> None:
        self.items=[]
        
    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self,item_name):
        new_items=[]
        removed=False
        for item in self.items:
            if item.name != item_name:
                new_items.append(item)
            else:
                removed=True
        self.items = new_items
        if removed:
            print('Successfully removed item ', item_name)
        else:
            print('Item not found:', item_name)
        
    def display_menu(self):
        print('Menu:')
        for item in self.items:
            print(item)
            
    # def __str__(self):
    #     print('Menu:')
    #     for item in self.items:
    #         print(item)
    #     return f'all done'

alo = Menu()
alo.add_item(MenuItem('kabab',12,'kabab may haddi')) 
alo.add_item(MenuItem('jabab',34,'jabab may haddi')) 
alo.add_item(MenuItem('nabab',42,'mabab may haddi')) 
alo.add_item(MenuItem('hgbab',62,'jgabab may haddi')) 
alo.add_item(MenuItem('labab',22,'labab may haddi')) 
alo.remove_item('kabab')
alo.display_menu()