#lambda

# def doubled(x):
#     return x*2

doubled = lambda num : num*4
squared = lambda num : num * num
result = doubled(44)
output=squared(9)
# print(result)
# print(output)

add= lambda x,y : x+y
r=add(4,5)
# print(r)

numbers = [12,56,94,456,34,634,24,67]

doubled_num = map(lambda x: x*2 ,numbers)
squared_num = map(lambda x: x*x ,numbers)
print(list(doubled_num))
print(list(squared_num))