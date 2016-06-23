from mentor import Mentor
from student import Student
from eki import Eki
import csv
import os



class CodecoolClass:

    def __init__(self, location, year, students=None, mentors=None, EKI_list=None):
        if students is None:
            students = []
        if EKI_list is None:
            EKI_list = []
        if mentors is None:
            mentors = []

        self.location = location
        self.year = int(year)
        self.students = students
        self.mentors = mentors
        self.EKI_list = EKI_list
        #print("Típusa: loc: %s, year: %s, stud: %s, ment: %s" % (type(location), type(year), type(students), type(mentors) ))

    @classmethod
    def generate_local(cls):
            print("Generating local CodecoolClass...")
            local_object = CodecoolClass("Budapest", 2016)
            #  print("Class Location: %s" % (cls.location))
            #  print("Year: %d" % ())
            students_path = os.path.abspath("./data/students.csv")
            with open(students_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Student(int(row[6]), int(row[7]), row[0], row[1], int(row[2]), row[3], int(row[4]), row[5])
                    local_object.students.append(instance)


            mentors_path = os.path.abspath("./data/mentors.csv")
            with open(mentors_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Mentor(row[6], int(row[7]), row[0], row[1], int(row[2]), row[3], int(row[4]), row[5])
                    local_object.mentors.append(instance)

            EKI_path = os.path.abspath("./data/eki.csv")
            with open(EKI_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    instance = Eki(row[0], int(row[1]), row[2])
                    local_object.EKI_list.append(instance)

                    #test
                    #test = [local_object.students, local_object.mentors, local_object.EKI_list]
                    #for test_subject in test:
                        #print("List: %s" % (test_subject))
                        #for i in test_subject:
                            #print(" Object name: %s. Object type: %s." % (i, type(i)))

            return local_object

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            if full_name.replace(" ", "").lowercase() == student.full_name.replace(" ", "").lowercase():
                return student
        raise NameError("Sorry man, this %s Fella is not in this class..." % (full_name))

    def find_mentor_by_full_name(self, full_name):
        for mentor in self.mentors:
            if full_name.replace(" ", "").lowercase() == student.replace(" ", "").lowercase():
                return mentor
        raise NameError("No luck, Dude, %s is ain't no teachin' in here!!!" % (full_name))
