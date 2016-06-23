from person import Person


class Student(Person):
    def __init__(self, knowledge_level, energy_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.knowledge_level = int(knowledge_level)
        self.energy_level = int(energy_level)

    def use_EKI(self, eki):
        if (eki.d_energy + eki.d_knowledge) > 0:
            print ("%s decided to use %s to raise his mood." % (self.first_name, eki.name))
        else:
            print ("something terrible happend: %s" % eki.name)
        input()
        eki.influence(self)

    def ask_for_help(self, mentor):
        mentor.teach(self)

    @classmethod
    def create_by_csv(file_name="students.csv"):
        student_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student_list.append(row)
        return(student_list)
