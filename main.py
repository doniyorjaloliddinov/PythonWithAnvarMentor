from person import Person
from professor import Professor
from students import Student
from math_professor import MathProfessor
from subject import Subjects

talaba = Student("rama", 2004, "male", 2)
talaba3 = Student("Sama", 2003, "female", 4)
sub = Subjects("Annita", 2005, "female", 3)
sub1 = Subjects("Anna", 2003, "female", 3)
sub2 = Subjects("Anny", 2004, "female", 3)

# print(sub)
sub.add_student()
sub1.add_student()

print(sub[-1])
print(Student)
# print(sub[1])s
# print(sub[0])
# print(talaba==talaba3)
# print(talaba)
# talaba2 = Student("Kama", 2004, "male")
# print(talaba.__gender)
# print(talaba.get_gender())
# print(talaba.get_cuantity_of_students())
# student1 = Student("Andrew", 1999)
# student1.register_to_subject("math")
# student1.register_to_subject("phisics")
# # print(student1.subjects)
# student1.remove_subject("math")
# print(student1.subjects)
# person = Person("marry", "Washington D.C", 1995, "light")
# print(person)
# print(person.get_cuantity_of_people())
# print(person.__skin_color)
# print(person.get_skin_color())
# professor = MathProfessor("Daniel","USA", 1992, "professor","math")
# print(professor.get_age(2024))
# print(professor.get_skin_color())
# print(professor.get_info())
# print(professor.ban_user())