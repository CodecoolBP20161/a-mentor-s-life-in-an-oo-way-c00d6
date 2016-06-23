import random
from student import Student


class Code:
    ASSIGNMENT_NAMES = ["Snake Game", "Fakkin' Hard Shit"]
    MAX_DIFFICULTY = 200
    MIN_DIFFICULTY = 0

    def __init__(self, name, difficulty):
        self.name = ASSIGNMENT_NAMES[random.randint(0, len(ASSIGNMENT_NAMES)-1)]
        self.difficulty = random.randint(0, 200)
        self.is_working = False

    def get_worked_on(self, student, is_working):
        print ("%s's assignement, the '%s' is ready, but he don't know if it's ok." % student.first_name, self.name)
        try_count = 0
        skill = (int(student.knowledge_level) + int(student.energy_level))
        print("Based on his attributes, %s's skill is %d. The difficulty of the assignment is %d." % (student.name, skill, self.name, self.difficulty))
        while try_count == 3:
            if skill > difficulty:
                print ("so, of course, it worked perfectly.")
                input()
                print ("The mentors's evaluation is:")
                print("Awesome, %s, the B0SS succesfully completed the %s assignment!" % (student.name, self.name))
                is_working = True
                return is_working
            else:
                try_count += 1
                print ("So, unfortunately, it couldn't run.")
                input ()
                print ("The mentors's evaluation is:")
                print("Try again,man! That wasn't even close for %s, to make the %s assignment!" % (student.name, self.name))
                input()
                print ("Poor %s, he has to do it again..." % student.first_name)
        student.ask_for_help()
