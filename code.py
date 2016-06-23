from random import randint
from student import Student
from codecool_class import CodecoolClass
codecool_bp = CodecoolClass.generate_local()


class Code:
    def __init__(self, difficulty, name=(["Snake Game", "Fakkin' Hard Shit"][randint(0, 1)])):
        self.name = name
        self.difficulty = difficulty

    def get_worked_on(self, student):
        print("%s's assignement, the '%s' is ready, but he don't know if it's ok." % (student.first_name, self.name))
        input()
        skill = (int(student.knowledge_level) + int(student.energy_level))
        print("Based on his attributes, %s's skill is %d. The difficulty of the assignment is %d." % (student.first_name, skill, self.difficulty))
        if skill > self.difficulty:
            print("so, of course, it worked perfectly.")
            input()
            print("The mentors's evaluation is:")
            print("Awesome, %s, the B0SS succesfully completed the %s assignment!" % (student.first_name, self.name))
        else:
            print("So, unfortunately, it couldn't run.")
            input()
            print("The mentors's evaluation is:")
            print("Try again,man! That wasn't even close for %s, to make the %s assignment!" % (student.first_name, self.name))
            input()
            print("Poor %s, he has to do it again..." % student.first_name)
            input()
            student.ask_for_help(codecool_bp.mentors[2], self.name)
