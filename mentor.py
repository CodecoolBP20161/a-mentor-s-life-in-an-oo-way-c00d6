from person import Person
from student import Student

class Mentor(Person):

    def __init__(self, nickname, teaching_level):
        self.nickname = nickname
        self.teaching_level = teaching_level

    def teach(self, student):
        student.knowledge_level += 3 * self.teaching_level
        if student.knowledge_level > 100:
            student_knowledge_level = 100
        student.energy_level -= 3 / self.teaching_level
        if student.energy_level > 100:
            student_energy_level = 100
        print ("I explain it now. Is it ok?")
        return student

    def check_energy_level(self, student_list):
        for student in student_list:
            if student.energy_level < 50:
                print ('%s says:' % self.nickname)
                print ('Dont worry, %s!  Be happy!' % student.first_name)
                student.energy_level = 100
        return student_list

    def check_mood(self, student_list):
        sum_mood = 0
        student_num = 0
        for student in student_list:
            sum_mood += student.mood
        if sum_mood/len(student_list) < 40:
            for student in student_list:
                student.mood = 100
        return student_list
            
