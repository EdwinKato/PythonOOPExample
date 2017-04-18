from Person import Person

class Student(Person):

    def __init__(self, name, surname, student_id):
        super(Student, self).__init__(name, surname)
        self.student_id = student_id
        self.course_units = []

    def enrol(self, course):
        self.course_units.append(course)

    def show_course_units(self):
        courses = (",").join(self.course_units)
        print "{0} enrolled for {1}".format(self.name, courses)