from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from code import Code


codecool_bp = CodecoolClass.generate_local()
#studenteket felsorolni, canvas szerint megcsinálni
print('Location: ', codecool_bp.location, '\nYear: ', codecool_bp.year, )
print('\nMentors: ')
for i in range(len(codecool_bp.mentors)):
    print('  ', codecool_bp.mentors[i].full_name)
print('\nStudents:')
for i in range(len(codecool_bp.students)):
    print('  ', codecool_bp.students[i].full_name)
input()
print("\nMentors arrive at school. They welcome students with a cheery smile\n")
input()
codecool_bp.mentors[1].check_energy_level(codecool_bp.students)
input()
codecool_bp.mentors[0].check_mood(codecool_bp.students)
input()
codecool_bp.students[3].use_EKI(codecool_bp.EKI_list[7])
input()
code = Code(215, "Fakkin' Hard Shit")
code.get_worked_on(codecool_bp.students[1])
