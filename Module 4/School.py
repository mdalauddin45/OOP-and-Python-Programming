class Student:
    def __init__(self,name,id,cls):
        self.name=name
        self.id=id
        self.cls=cls
    
    # string return kory repr
    def __repr__(self)->str:
        return f'student with name {self.name}, class: {self.cls}, id: {self.id}'

class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    
    def __repr__(self) -> str:
        return f'Teahcer : {self.name}, Subject: {self.subject}, id: {self.id}'

class School:
    def  __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]
        
    def add_teacher(self,name,sub):
        id = len(self.teachers)+101
        teacher = Teacher(name,sub,id)
        self.teachers.append(teacher)
        # print(f'{name} successfuly added in teacher, you teach in student {sub} , your teacher id : {id}')
    
    def enroll(self,name,fee):
        if fee<6500:
            print(f'{name} you have not Enough fee')
        else:
            id=len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            # print(f'{name} is enrolled with id {id}, extra monry {fee-6500}')
    def __repr__(self) -> str:
        print('welcome to ',self.name)
        print('-------OUR TEACHERA------')
        for teacher in self.teachers:
            print(teacher)
        print('------OUT STUDENT------')
        for student in self.students:
            print(student)
        return 'All done now'

# alia = Student('alia torkari',9,4)
# ranbir = Teacher('Ranbir kapur','Chemistry', 999)
# print(alia)
# print(ranbir)

phitron = School('phitron')
phitron.enroll('alia',8000)
phitron.enroll('kalia',6600)
phitron.enroll('balia',8500)
phitron.enroll('salia',6500)

phitron.add_teacher('Mr Assaduzzan Apu','c')
phitron.add_teacher('Mr Rahat khan phatan ','c++')
phitron.add_teacher('Mr Zankar mahbub ','Phyton')
phitron.add_teacher('Mr Manjur alam','DS')
print(phitron)