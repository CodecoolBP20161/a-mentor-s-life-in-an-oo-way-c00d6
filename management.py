from person import Person
from student import Student
from codecool_class import CodecoolClass


class Management(Person):

    def _init_(self, name):
        self.name = name

    def change_life(self, mentors, students):
        print("Management is in the air!")
        input()
        if self.full_name == "Boda Józsi":
            print("Boda Józsi levitates in.")
            print('''Boda Józsi: "I have arrived, people of Codecool! I give you my infinite energy and knowledge! Use it wisely!" ''')
            input()
            for i in range(len(students)):
                students[i].energy_level = 100
                students[i].stress = 0
                students[i].knowledge_level = 100
            print('''The students feel that their confidence is growing!! They can achieve anything!
No more stress!! They are full of energy!! Nothing can stop them!''')
            input()
            for i in range(len(mentors)):
                mentors[i].stress = 0
                mentors[i].teaching_level = 100
            print('''The mentors feel peace in their hearts! They can even teach a dog to code!!! Life has become so easy since Józsi is here.
Their teaching level has set to maximum, they dont even know the word "stress" anymore!! ''')
            input()
            print('''Boda Józsi: "I have to go now,my beloved people! But soon, I'll be back! Until then, I want success from you!!"
Boda Józsi levitates out.''')

    def creeping(self, mentors, students):
        if self.full_name == "Creepy Guy":
            print("What is this? Something is happening in the office. The atmosphere is changed!!! (0.0) ")
            input()
            for i in range(len(students)):
                students[i].stress += 20
            print('''The students have a strange feeling that something (or somebody?) is behind their back.
When they look behind,they dont see anything!! That's creepy! Their stress level is increased by 20.''')
            input()
            for i in range(len(mentors)):
                mentors[i].stress += 30
                mentors[i].teaching_level += 30
            print('''The mentors have the same feeling! Does someone is watching them??
Their stress level is also increased by 30 !!! ''')
            input()
            print('''OH!! It's just CreepyGuy!! He has come to teach the mentors!! Their teaching level is increased by 30 !!
You scared us, CreepyGuy! ''')
