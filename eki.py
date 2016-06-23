from person import Person
from student import Student

class Eki:

    def __init__(self, name, d_energy, d_knowledge):
        self.d_energy = int(d_energy)
        self.d_knowledge = int(d_knowledge)
        self.name = name

    def influence(self, student):
        print ("%s's energy was %i, knowledge was %i" % (student.first_name, student.energy_level, student.knowledge_level))
        student.knowledge_level += int(self.d_knowledge)
        if student.knowledge_level > 100:
            student_knowledge_level = 100
        if student.knowledge_level < 0:
            student_knowledge_level = 0
        student.energy_level += int(self.d_energy)
        if student.energy_level > 100:
            student_energy_level = 100
        if student.energy_level < 0:
            student_energy_level = 0
        print ("now, energy is %i.  knowledge is %i" % (student.energy_level, student.knowledge_level))
        return student
