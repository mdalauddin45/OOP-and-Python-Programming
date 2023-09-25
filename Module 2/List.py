#list array, collection is same (simple terms)
#index     0  1  2  3  4  5  6   7  8 9 10 11 12
numbers = [34,64,32,64,47,38,79,34,75,86,8,78,90]
#index  = -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(numbers[3], numbers[-3]) 

#list (start:end)
print(numbers[2:4]) #return an array
#list (start:end:step)
print(numbers[2:7:2])
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[2:])
print(numbers[:7])
print(numbers[:]) #shortcut to copy a list
print(numbers[::-1]) #shortcur reverse a list
