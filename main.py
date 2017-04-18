from Student import Student
from Student import Student
from StaffMember import StaffMember

lubega = Student("Lubega", "Deus", 90)
lubega.enrol("Accounting")
lubega.enrol("Business law")
lubega.setStudentId(9)
lubega.show_course_units()
lubega.display_no_of_people()

Kizito = StaffMember("Kizito","Edward")
Kizito.add_course("Luganda")
Kizito.add_course("Swahili")
Kizito.show_courses_taught()
Kizito.display_no_of_people()