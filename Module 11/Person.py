import random
class Person:
    def __init__(self,name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name,subject) -> None:
        self.subject=subject
        super().__init__(name)
    
    def teach(self):
        pass
    
    def take_exam(self,subject,students):
        for student in students:
            marks = random.randint(0,100)
            #todo set marks for the subject each student

class Student(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__id=None
        self.calssroom = None
        self.subjects = []
        self.marks = {}
        self.grade = None
    @property   
    def id(self):
        return self.__id
    
    def id(self,value):
        self.__id ==value
        