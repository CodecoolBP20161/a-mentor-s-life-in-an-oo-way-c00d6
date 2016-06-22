from person import Person
from student import Student

class Eki:

    def __init__(self, d_energy, d_knowledge, name):
        self.d_energy = d_energy
        self.d_knowledge = d_knowledge
        self.name = name

    def influence(self, student):
        student.knowledge_level += self.d_knowledge
        if student.knowledge_level > 100:
            student_knowledge_level = 100
        if student.knowledge_level < 0:
            student_knowledge_level = 0
        student.energy_level += self.d_energy
        if student.energy_level > 100:
            student_energy_level = 100
        if student.energy_level < 0:
            student_energy_level = 0
        print ("%s used" % self.name)
        print ('energy: %i.  knowledge: %i' % (student.energy_level, student.knowledge_level))
        return student
