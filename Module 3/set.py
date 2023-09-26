#set is a unique collection . no duplicates
# list--> []
# tuple--> ()
# set--> {}
numbers = [12,56,94,456,34,634,24,67]
# numbers.add(55) // do not add this number
numbers.append(100)
# print(numbers)
numbers_set= set(numbers)
numbers_set.add(30)
# numbers_set.append(30)// dont append this numbers set
# print(numbers_set)
numbers_set.remove(12)
# print(numbers_set)

A={1,3,5}
B={1,2,3,4,5}
print( A & B) #A!UB
print( A | B)  #AUB