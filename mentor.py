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

    def teach(self, student, code):
        print("%s says:" % student.first_name)
        print("%s, could you explain it please?" % self.nickname)
        input()
        print("As a perfect mentor, %s can explain amazingly, how to solve the %s" % (self.nickname, code))
        input()
        new_knowledge_level = student.knowledge_level + 3 * self.teaching_level
        if student.knowledge_level > 100:
            student_knowledge_level = 100
        new_energy_level = student.energy_level - 3 / self.teaching_level
        if student.energy_level < 0:
            student_energy_level = 0
        print("With %s's help, %s could improve his skills:" % (self.nickname, student.first_name))
        print("energy level from %i to %i, knowledge level from %i to %i" % (student.energy_level, new_energy_level, student.knowledge_level, new_knowledge_level))
        return student

    def check_energy_level(self, student_list):
        for student in student_list:
            if student.energy_level < 50:
                print("%s realizes that %s's energy level is critically low." % (self.nickname, student.first_name))
                input()
                print('%s says:' % self.nickname)
                print('Dont worry, %s!  Be happy!' % student.first_name)
                input()
                student.energy_level = 100
                print("\n%s's energy level is %i now, thanks for %s" % (student.first_name, student.energy_level, self.nickname))
        return student_list

    def check_mood(self, student_list):
        print("Today, it's %s's job to take care of the mood in the class.\n" % self.nickname)
        mood = 0
        sum_mood = 0
        student_num = 0
        for student in student_list:
            mood = student.energy_level + student.knowledge_level - student.stress
            sum_mood += mood
        average_mood = (sum_mood/len(student_list))
        print("According to his calculations, the avarage mood of the class is %i" % average_mood)
        input()
        print("%s says:" % self.nickname)
        if average_mood > 150:
            print("The class mood is excellent, you are so amazing! I want to spend my life with you!!!!!!")
        if average_mood > 50 and average_mood < 150:
            print("I can see, that class mood is ok.")
        if average_mood < 50:
            print("Come on, let's do something. You should drink a coffee or go to a meetup.")
            print("Ask Csibi to smile, eat gyros, do yoga! You have so many possibilities!")
        return student_list
