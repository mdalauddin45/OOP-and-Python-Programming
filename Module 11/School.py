class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.teachers = {}
        #composition
        self.classrooms={}
    
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom 
    
    def student_admission(self,student,classroom_name):
        if classroom_name in self.classrooms:
            #TODO set student ID 
            self.classrooms[classroom_name].add_student(student)
            # student.id = 
        else:
            print(f'No classroom as named {classroom_name}')
    
    def add_teacher(self,subject,teacher):
        self.teachers[subject]= teacher

class ClassRoom:
    def __init__(self,name) -> None:
        self.name=name
        self.students=[]
        
    def add_student(self,student):
        serial_id = f'{self.name}--{len(self.students)+1}'
        student.id = serial_id
        student.clssroom =self.name
        self.students.append(student)
    
    def __str__(self) -> str:
        return f'{self.name}--{len(self.students)}'

    def get_top_students(self):
        pass