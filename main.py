from Student import Student
from StaffMember import StaffMember

lubega = Student("Lubega", "Deus", 90)
lubega.enrol("Accounting")
lubega.enrol("Business law")
lubega.setStudentId(9)
lubega.show_course_units()
lubega.display_no_of_people()
print lubega.get_access_level() #Polymorphism access level behaves different depending on caller
#print lubega.__student_id id is private and cant be accessed here

Kizito = StaffMember("Kizito","Edward")
Kizito.add_course("Luganda")
Kizito.add_course("Swahili")
Kizito.show_courses_taught()
Kizito.display_no_of_people()
print Kizito.get_access_level()

#name is public and thus can be accessed here
print Kizito.name
