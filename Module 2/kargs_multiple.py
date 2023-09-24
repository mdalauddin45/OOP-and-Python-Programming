def full_name(first,last):
    name = f'full name is {first}{last}'
    return name
name = full_name('ala ','uddin')
name1 = full_name(last=' ala',first='uddin')
# print(name)
# print(name1)

# def famous_name(first,last,title,addition):
#     name=f'{title}{first}{last}{addition}'
#     return name

# fname=famous_name('ala','uddin','md','dev')
# print(fname)

# def famous_name(first,last,**addition):
#     name=f'{first}{last}'
#     # print(addition['title'])
#     for key,value in addition.items():
#         print(key,value)
#     return name


# fname=famous_name(first='ala',last='uddin',last1='hello',title='md',title2='mohsmm',addition='dev',adition2='tev')
# print(fname)


def a_lot(num1,num2):
    sum=num1+num2
    mul=num2*num1
    remian=num1 - num2
    return sum,mul,remian
everything = a_lot(43,32)
print(everything)