numbers=[12,42,54,24,64,75,78,97]
person=['kala chan','kalipur',23, 'studen']
# key value pair
# #dictionary 
# #object 
# #has table 
# #overalp with set 
#{key:value}
person={'name': 'kala pakhi', 'Address': 'kalia phur','Age': 23, 'job': 'faceBooker'}
# print(person)
# print(person['job'])
# print(person.keys())
# print(person.values())
person['language']='python'
person['name']='Shada Pakhi'
del person['Age']
# print(person.keys())
# print(person.values())

#special dictonary looping
# for i in person.items():
#     print(i)
for key,Value in person.items():
    print(key,Value)