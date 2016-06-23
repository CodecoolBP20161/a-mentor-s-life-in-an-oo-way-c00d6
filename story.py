from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student


codecool_bp = CodecoolClass.generate_local()
print(codecool_bp.mentors[1].full_name)
print ('Location: ', codecool_bp.location, 'Year: ', codecool_bp.year, )
print ('Mentors: ')
for i in range(len(codecool_bp.mentors)):
    print ('  ', codecool_bp.mentors[i].full_name)
#print (Mentor.create_by_csv()) #mentorok and you
#input("")
print ("Mentors arrives at school. They welcome students with cheery smile")
mentor_list[1].check_energy_level(student_list)
input()
mentor_list[0].check_mood(student_list) #stresszt beállítani kb 80ra, k_l 0-ra, hogy rossz legyen a mood
input()
