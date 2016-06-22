from person import Person
from mentor import Mentor
from code import Code


class Student(Person):
    def __init__(self, knowledge_level, energy_level):
        Person.__init__(self, *args, **kwargs)
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    def use_EKI(self, eki):
        print("%s energy and knowledge level under the frog's ass, that's why %s uses an EKI" % (self.name, self.name))
        eki.influence(self)

    def ask_for_help(self, mentor):
        mentor.teach(self)

    @classmethod
    def create_by_csv():
        student_list = []
        path = os.path.abspath("./data/students.csv")
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student_list.append(row)
        print(student_list)
