from person import Person
from student import Student
from codecool_class import CodecoolClass


class Management(Person):

    def _init_(self, name):
        self.name = name

    def change_life(self, mentors=CodecoolClass.mentors, students=CodecoolClass.students):
        if self.name == "Boda Józsi":
            
            print('Boda Józsi has arrived!')
            for student, mentor in students, mentors:
                student.energy_level = 100
                student.stress = 0
                students.knowledge_level = 100
                mentors.stress = 0
                mentors.teaching_level = 100

    def creepy_guy(self, mentors=CodecoolClass.mentors, students=CodecoolClass.students):
        for student, mentor in students, mentors:
            student.stress += 20
            mentors.stress += 30
            mentors.teaching_level += 30
