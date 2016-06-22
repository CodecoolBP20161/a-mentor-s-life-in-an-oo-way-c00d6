from mentor import Mentor
from student import Student
import csv
import os
class CodecoolClass:

    def __init__(self, location, year, students=[], mentors=[], EKI_list=[]):
        self.location = location
        self.year = int(year)
        self.students = students
        self.mentors = mentors
        self.EKI_list = EKI_list
    @classmethod
    def generate_local(cls):
            Local_Object = CodecoolClass.__init__(cls, "Budapest", 2016)

            students_path = os.path.abspath("./data/students.csv")
            with open(students_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Student(row[0], row[1], int(row[2]), row[3], int(row[4]), int(row[5]), row[6])
                    cls.students.append(instance)

            mentors_path = os.path.abspath("./data/mentors.csv")
            with open(mentors_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Mentor(row[0], row[1], int(row[2]), row[3], int(row[4]), int(row[5]), int(row[6]))
                    cls.mentors.append(instance)

            EKI_path = os.path.abspath("./data/eki.csv")
            with open(students_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Eki(int(row[0]), int(row[1]), row[2])
                    cls.EKI_list.append(instance)
            return Local_Object




    def find_student_by_full_name(self, full_name):
        for student in self.students:
            if full_name.replace(" ", "").lowercase() ==  student.full_name.replace(" ", "").lowercase():
                return student
        raise NameError("Sorry man, this %s Fella is not in this class..." % (full_name))

    def find_mentor_by_full_name(self, full_name):
        for mentor in self.mentors:
            if full_name.replace(" ", "").lowercase() ==  student.replace(" ", "").lowercase():
                return mentor
        raise NameError("No luck, Dude, %s is ain't no teachin' in here!!!" % (full_name))
