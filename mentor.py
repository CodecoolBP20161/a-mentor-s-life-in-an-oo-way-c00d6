from person import Person
from student import Student
import os
import csv

class Mentor(Person):

    def __init__(self, nickname, teaching_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nickname = nickname
        self.teaching_level = teaching_level


    @classmethod
    def create_by_csv(file_name="mentors.csv"):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentor_list.append(row)
        return(mentor_list)

    def teach(self, student):
        student.knowledge_level += 3 * self.teaching_level
        if student.knowledge_level > 100:
            student_knowledge_level = 100
        student.energy_level -= 3 / self.teaching_level
        if student.energy_level < 0:
            student_energy_level = 0
        print("I explain it now. Is it ok?")
        return student

    def check_energy_level(self, student_list):
        for student in student_list:
            if student.energy_level < 50:
                print('%s says:' % self.nickname)
                print('Dont worry, %s!  Be happy!' % student.first_name)
                student.energy_level = 100
        return student_list

    def check_mood(self, student_list):
        mood = 0
        sum_mood = 0
        student_num = 0
        for student in student_list:
            mood = student.energy_level + student.knowledge_level - student.stress
            sum_mood += mood
        average_mood = (sum_mood/len(student_list))
        if average_mood > 150:
            print("The class mood is excellent, you are so amazing! I want to spend my life with you!!!!!!")
        if average_mood > 50 and average_mood < 150:
            print("I can see, that class mood is ok.")
        if average_mood < 50:
            print("Come on, do something. You should drink a coffee or go to a meetup.")
            print(" Ask Csibi to smile, eat gyros, do yoga! You have so many possibilities!")
        return student_list
