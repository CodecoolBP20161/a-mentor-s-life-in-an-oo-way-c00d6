from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from code import Code


codecool_bp = CodecoolClass.generate_local()
print ('Location: ', codecool_bp.location, 'Year: ', codecool_bp.year, )
print ('Mentors: ')
for i in range(len(codecool_bp.mentors)):
    print ('  ', codecool_bp.mentors[i].full_name)
input()
print ("\nMentors arrives at school. They welcome students with cheery smile\n")
input()
codecool_bp.mentors[1].check_energy_level(codecool_bp.students)
input ()
codecool_bp.mentors[0].check_mood(codecool_bp.students)
input()
codecool_bp.students[3].use_EKI(codecool_bp.EKI_list[7])
input()
code.get_worked_on(student[1], is_working)
