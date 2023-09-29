def address(*argv):
      	for i in argv:
               	print(i)
address ('Name: Alauddin ', 'id : 220239013', 'Semester: 3rd ', 'sec: A')

def Address(**kwargs):
      	for key, value in kwargs.items():
               	print(f'{key} : {value}')
Address(name='Alauddin', id='220239013', semester='3rd ',sec='A')
