numbers=[10,20,30,40,20]
numbers.append(50)
print(numbers)
#inset(index,value)
numbers.insert(3,32)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.reverse()
print(numbers)
#remove last index
numbers.pop()
print(numbers)
l=numbers.index(40)
print(l)
numbers.sort()
print(numbers)
num=numbers.copy()
print(num)