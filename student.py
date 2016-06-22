from person import Person
from mentor import Mentor
from code import Code
import os
import csv


class Student(Person):
    def __init__(self, knowledge_level, energy_level):
        Person.__init__(self, *args, **kwargs)
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level



    def use_EKI(name):
        pass

    def ask_for_help(self, mentor):
        mentor.teach(self)
        print("MUUUUKODIK")

peti = Student
print(peti.open_student_csv())
peti.ask_for_help()
