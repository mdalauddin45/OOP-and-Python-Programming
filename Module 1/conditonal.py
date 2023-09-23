a=4
# if a > 5: print('5 er besi')
# elif a>3: print('3 er boro')
# else: print('5 er kom')
boss = True
if boss is True: print('tel er bakso niya astyci ')
else: print('pory astyci')

#nested condition 
coin = 'head'
if boss == True:
    print('boss you are joss ')
    if coin == 'tail': 
        print("batting")
    else: 
        print("bowling")
        if(5>3) and 3<5 or 3!=2:
            print("5 boro")
        else: print('5 er kom')
else: print('you are lose not a boss')