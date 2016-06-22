from mentor import Mentor
from student import Student


class CodecoolClass:
    
    def open_student_csv():
        student_list = []
        path = os.path.abspath("./data/students.csv")
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student_list.append('-'.join(row))
        return student_list[0]
    pass
